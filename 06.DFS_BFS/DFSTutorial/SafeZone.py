dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):
    check_list[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and check_list[xx][yy] == 0 and height_list[xx][yy] > h:
            dfs(xx, yy, h)


n = int(input())
height_list = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
res = 0
# 높이 0 - 100
for h in range(100):
    # 높이 지정될 때마다 체크리스트 새로 생성
    check_list = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check_list[i][j] == 0 and height_list[i][j] > h:
                cnt += 1
                dfs(i, j, h)

    res = max(res, cnt)
    # 주어진 지역보다 큰 높이 탐색시 반복문 탈출
    if cnt == 0:
        break

print(res)