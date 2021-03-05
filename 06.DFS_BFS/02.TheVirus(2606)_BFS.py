import sys
from collections import deque

def bfs(v):
    global cnt
    queue = deque([v])
    visited[v] = True
    while queue:
        for i in graph[queue.popleft()]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cnt = 0
graph = [[] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * len(graph)

bfs(1)
print(cnt)
