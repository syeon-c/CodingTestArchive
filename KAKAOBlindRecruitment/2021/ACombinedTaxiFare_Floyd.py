import sys


# 비용(S - T) + 비용(T - A) + 비용(T - B) 의 최솟값 구하
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    answer = INF
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0
    for i in fares:
        graph[i[0] - 1][i[1] - 1] = i[2]
        graph[i[1] - 1][i[0] - 1] = i[2]

    for t in range(n):
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    temp = min(graph[i][j], graph[i][t] + graph[t][j])
                    graph[i][j] = graph[j][i] = temp

    for t in range(n):
        temp = graph[s - 1][t] + graph[t][a - 1] + graph[t][b - 1]
        answer = min(answer, temp)

    return answer


n = 6
s = 4
a, b = 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))

