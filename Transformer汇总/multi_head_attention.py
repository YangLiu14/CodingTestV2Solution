"""
Super simplified MHA

1. 定义Q, K, V的shape (B, seq_len, embed_dim)
2. 经过Linear层 (embed_dim 分为 n_heads个的 head_dim)
3. Attention
4. FC层

这里没有考虑positional encoding
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, n_heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = n_heads
        # embed_size 是最终的tensor的channel_size
        # 因为要分开在n个heads里面去计算, 所以每个head里面计算的channel_dim都是head_dim
        self.head_dim = embed_size // n_heads

        self.v_proj = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.k_proj = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.q_proj = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_out = nn.Linear(self.embed_size, self.embed_size)

    def forward(self, query, key, value):
        """
        Args:
            query:  (B, q_len, embed_dim)
            key:   (B, k_len, embed_dim)
            value: (B, v_len, embed_dim)

        """
        B = query.shape[0]
        len_q, len_k, len_v = query.shape[1], key.shape[1], value.shape[1]  # sequence length
        # len_k == len_v

        # Split embeddings into self.heads pieces (embed_size --> n_heads * head_dim)
        query = query.reshape(B, len_q, self.n_heads, self.head_dim)
        key = key.reshape(B, len_k, self.n_heads, self.head_dim)
        value = value.reshape(B, len_v, self.n_heads, self.head_dim)

        # Apply linear transformation (separately for each head)
        queries = self.q_proj(query).transpose(1, 2)  # (B, n_heads, len_q, head_dim)
        keys = self.k_proj(key).transpose(1, 2)
        values = self.v_proj(value).transpose(1, 2)

        # Attention
        # (B, nh, len_q, dim) * (B, nh, dim, len_k) --> (B, nh, len_q, len_k)
        sqrt_dk = torch.sqrt(torch.tensor(self.head_dim))
        attention = torch.matmul(queries, keys.transpose(-2, -1)) / sqrt_dk  # (B, nh, len_q, len_k)
        attention = F.softmax(attention, dim=-1)

        # Apply attention weights to values
        # (B, nh, len_q, len_k) * (B, nh, len_v, dim) --> (B, nh, len_q, dim)
        out = torch.matmul(attention, values).transpose(1, 2)  # (B, len_q, nh, dim)
        out = out.reshape(B, len_q, self.embed_size)

        # Final Linear layer
        out = self.fc_out(out)

        return out


class TransformerBlock(nn.Module):
    def __init__(self, embed_size, n_heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = MultiHeadAttention(embed_size, n_heads)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)

        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, forward_expansion * embed_size),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_size, embed_size),
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value):
        attention = self.attention(query, key, value)
        x = self.norm1(attention + query)
        x = self.dropout(x)
        forward = self.feed_forward(x)
        x = self.norm2(forward + x)  # residual
        out = self.dropout(x)
        return out


class Encoder(nn.Module):
    def __init__(self, embed_size, num_layers, n_heads, forward_expansion, dropout):
        super(Encoder, self).__init__()
        self.embed_size = embed_size
        self.layers = nn.ModuleList(
            TransformerBlock(
                embed_size,
                n_heads,
                dropout=dropout,
                forward_expansion=forward_expansion
            ) for _ in range(num_layers)
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.dropout(x)

        for layer in self.layers:
            out = layer(query=x, key=x, value=x)  # self-attention

        return out


