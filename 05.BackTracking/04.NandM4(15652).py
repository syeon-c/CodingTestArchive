import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
result = []


def DFS(x, y):
    if x == m:
        print(*result)
        return

    for i in range(y, n):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)

            DFS(x + 1, y + 1)

            visited[i] = False
            result.pop()


DFS(0, 0)