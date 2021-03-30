def dfs(x):
    if x > 0:
        dfs(x - 1)
        print(x, end=' ')


n = int(input())
dfs(n)