from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접 노드들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 4, 8],
    [1, 3],
    [2],
    [1, 5, 7],
    [4, 6],
    [5],
    [4],
    [1, 9],
    [8]
]

# 각 노드의 방문 정보 리스트로 표현
visited = [False] * len(graph)
bfs(graph, 1, visited)
