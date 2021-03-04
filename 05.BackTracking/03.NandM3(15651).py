import sys

n, m = map(int, sys.stdin.readline().split())
result = []


def DFS(x):
    if x == m:
        print(*result)
        return

    for i in range(n):
        result.append(i + 1)
        DFS(x + 1)
        result.pop()


DFS(0)
