from collections import deque

n = int(input())
map_list = [list(map(int, input().split())) for _ in range(n)]
# 왼쪽(-1, 0)에서부터 시계 방향으로 방향 표시
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if map_list[i][j] == 1:
            map_list[i][j] = 0
            Q.append((i, j))
            # BFS 탐색
            while Q:
                tmp = Q.popleft()
                # tmp의 상하좌우, 대각선에 섬이 있는지(1) 확인
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    # 지도의 범위에 벗어나지 않으면서 섬이 있으면
                    if 0 <= x < n and 0 <= y < n and map_list[x][y] == 1:
                        # 방문 표시 해주고 큐에 추가
                        map_list[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)