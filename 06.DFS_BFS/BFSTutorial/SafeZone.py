from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
cnt = 0
res = 0
height_list = [list(map(int, input().split())) for _ in range(n)]
Q = deque()

for h in range(100):
    # 높이 새로 지정될 때마다 체크리스트와 cnt값 새로 설정
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않았고, 주어진 높이보다 값이 크면
            if check[i][j] == 0 and height_list[i][j] > h:
                # 방문 표시하고 큐에 추가
                check[i][j] = 1
                Q.append((i, j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and check[x][y] == 0 and height_list[x][y] > h:
                            check[x][y] = 1
                            Q.append((x, y))
                cnt += 1
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)