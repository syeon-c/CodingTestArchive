import sys

n, m = map(int, sys.stdin.readline().split())
nums = [1 + i for i in range(n)]
checkList = [False] * n
result = []


def DFS(x):
    if x == m:
        print(*result)

    for i in range(n):
        if checkList[i]:
            continue

        result.append(nums[i])
        checkList[i] = True

        DFS(x + 1)

        result.pop()
        checkList[i] = False


DFS(0)
