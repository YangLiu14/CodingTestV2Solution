"""
Dijstra的python实现
参考：https://yxudong.github.io/Dijkstra-%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E7%AE%97%E6%B3%95-Python-%E5%AE%9E%E7%8E%B0/

对应LeetCode 743. 网络延迟时间
"""


def dijkstra(times, n, k):
    """
    Args:
        times: List[tuple], [(src_node, dst_node, time]]
               保存从起始节点到目标节点的耗时
        n: (int) 一共有多少个节点, 编号从1开始
        k: (int) 起始节点
    """
    # 从任意一个node到另一个node所需要的时间, 存储为二维数组
    g = [[float('inf')] * n for _ in range(n)]
    for x, y, t in times:
        g[x - 1][y - 1] = t  # 初始化起点到其相邻节点的路径信息

    dist = [float('inf')] * n  # 用来记录从起点k到节点i的最短路径
    dist[k - 1] = 0
    used = [False] * n

    for _ in range(n):
        x = -1
        # 在所有的没有遍历过的节点中，取路径最小的（贪心）对应的node, x
        # 这里保证了"连通性", 是因为没有连通的节点的dist=inf
        for y, u in enumerate(used):
            if not u and (x == -1 or dist[y] < dist[x]):
                x = y
        # 如果used数据里面没有未使用的数据, x保持-1
        used[x] = True
        for y, t in enumerate(g[x]):
            # 找到从x出发, 其最近的相邻节点y, 并更新dist[y]
            dist[y] = min(dist[y], dist[x] + t)

    ans = max(dist)
    return ans if ans < float('inf') else -1
