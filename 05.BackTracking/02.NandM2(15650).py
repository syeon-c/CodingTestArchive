import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
result = []


def DFS(x):
    if x == m:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)

            DFS(x + 1)

            result.pop()

            for j in range(i+1, n):
                visited[j] = False


DFS(0)