import sys


def operation(i, a, b):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    elif i == 3:
        if a < 0:
            ans = (abs(a) // b)
            return -ans
        else:
            return a // b


def dfs(cnt, val):
    global min_res, max_res

    if cnt == n:
        max_res = max(val, max_res)
        min_res = min(val, min_res)
        return

    for i in range(4):
        if op[i] > 0:
            val = operation(i, nums[cnt], nums[cnt + 1])
            op[i] -= 1
            dfs(cnt + 1, val)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_res = float('Inf')
min_res = float('-Inf')

dfs(0, nums[0])

print(max_res)
print(min_res)
