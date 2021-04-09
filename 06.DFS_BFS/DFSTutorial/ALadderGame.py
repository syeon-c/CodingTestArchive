def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and ladder[x][y - 1] == 1 and ch[x][y - 1] == 0:
            dfs(x, y - 1)
        elif y + 1 < 10 and ladder[x][y + 1] == 1 and ch[x][y + 1] == 0:
            dfs(x, y + 1)
        else:
            dfs(x - 1, y)


ladder = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]

for i in range(10):
    if ladder[9][i] == 2:
        dfs(9, i)
