import sys
from collections import deque


# 깊이 우선 탐색, 인자는 시작 정점의 번호
def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for j in graph[start]:
        if not visited[j]:
            dfs(j)


# 너비 우선 탐색, 인자는 시작 정점의 번호
def bfs(start):
    queue = deque([start])
    visited[start] = False
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for j in graph[node]:
            if visited[j]:
                queue.append(j)
                visited[j] = False


# N은 정점의 개수,  M은 간선의 개수, V는 탐색을 시작할 정점의 번호
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
# 그래프 요소 오름차순 정렬
for i in range(len(graph)):
    graph[i].sort()
# 각 노드의 방문 정보 리스트로 표현
visited = [False] * len(graph)

dfs(v)
print()
bfs(v)
