import heapq


def printGraph(graph):
    for i in range(len(graph)):
        print(graph[i])


def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    for x, y, z in fares:
        graph[x].append((y, z))
        graph[y].append((x, z))

    # printGraph(graph)

    def dijkstra(start):
        distance = [INF] * (n + 1)
        distance[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            fare, now = heapq.heappop(heap)
            if distance[now] < fare:
                continue

            for i, j in graph[now]:
                cost = fare + j
                if distance[i] > cost:
                    distance[i] = cost
                    heapq.heappush(heap, (cost, i))
        return distance

    minFare = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # printGraph(minFare)
    answer = INF
    for i in range(1, n+1):
        answer = min(minFare[i][s] + minFare[i][a] + minFare[i][b], answer)

    return answer


n = 6
s = 4
a, b = 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))
