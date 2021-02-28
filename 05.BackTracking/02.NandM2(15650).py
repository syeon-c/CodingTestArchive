import sys

n, m = map(int, sys.stdin.readline().split())
nums = [1 + i for i in range(n)]
visited = [False] * n
result = []


def DFS(x, idx):
    if x == m:
        print(*result)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])

            DFS(x + 1, idx + 1)

            visited[i] = False
            result.pop()


DFS(0, 0)
