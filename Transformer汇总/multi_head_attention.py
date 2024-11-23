"""
Super simplified MHA
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

