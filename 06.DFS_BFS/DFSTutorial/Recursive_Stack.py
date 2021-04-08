def dfs1(x):
    if x > 0:
        dfs1(x - 1)
        print(x, end=' ')


def dfs2(x):
    if x > 0:
        print(x, end=' ')
        dfs2(x - 1)


n = 4
dfs1(n)
print()
dfs2(n)
