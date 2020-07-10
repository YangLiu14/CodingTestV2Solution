"""common.py: common tools"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            # new nodes are added to end of queue
            queue.extend(graph[vertex] - visited)
    return visited


def dfs(graph, root):
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
