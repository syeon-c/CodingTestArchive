import sys

n, m = map(int, sys.stdin.readline().split())
result = []


def DFS(x, y):
    if x == m:
        print(*result)
        return

    for i in range(y, n):
        result.append(i + 1)
        DFS(x + 1, y + 1)
        result.pop()


DFS(0, 0)
