import heapq
import sys


def solution(n, s, a, b, fares):
    INF = sys.maxsize
    graph = [[] for _ in range(n + 1)]
    for a, b, c in fares:
        graph[a].append((c, b))
        graph[b].append((c, a))

    def dijkstra(s):
        distance = [INF] * (n + 1)
        distance[s] = 0

        heap = []
        heapq.heappush(heap, (0, s))
        while heap:
            fare, now = heapq.heappop(heap)
            if distance[now] < fare:
                continue
