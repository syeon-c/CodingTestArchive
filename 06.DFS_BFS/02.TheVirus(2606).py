import sys


def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cnt = 0
graph = [[] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * len(graph)

dfs(1)
print(cnt)
