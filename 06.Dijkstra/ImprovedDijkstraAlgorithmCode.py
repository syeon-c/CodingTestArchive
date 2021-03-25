import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
s = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c  = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(s):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        # 가장 최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        #  이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드 거쳐서, 다른 노드로 이동하는 거리 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(s)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한으로 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])