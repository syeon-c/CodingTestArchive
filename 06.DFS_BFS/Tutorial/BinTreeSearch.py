def dfs_search_left(x):
    if x > 7:
        return
    else:
        print(x, end=' ')
        dfs_search_left(x * 2)
        dfs_search_left(x * 2 + 1)


def dfs_search_parent(x):
    if x > 7:
        return
    else:
        dfs_search_parent(x * 2)
        print(x, end=' ')
        dfs_search_parent(x * 2 + 1)


def dfs_search_right(x):
    if x > 7:
        return
    else:
        dfs_search_right(x * 2)
        dfs_search_right(x * 2 + 1)
        print(x, end=' ')


dfs_search_left(1)
print()
dfs_search_parent(1)
print()
dfs_search_right(1)
