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
            result.append(i + 1)
            print(result)
            DFS(x + 1)

            visited[i] = False
            result.pop()


DFS(0)
