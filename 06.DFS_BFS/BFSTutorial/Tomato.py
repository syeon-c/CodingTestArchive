from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
# 모든 토마토가 익는 날짜 기록 위한 리스트
day = [[0] * n for _ in range(m)]
Q = deque()

# 익은 토마토 큐에 삽입
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            Q.append((i, j))

while Q:
    x, y = Q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 인접 토마토가 익지 않았다면
        if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 0:
            # 인접 토마토 날짜 더해주고 익었음(1) 표시, 다시 큐에 삽입
            day[nx][ny] = day[x][y] + 1
            box[nx][ny] = 1
            Q.append((nx, ny))

# 모든 토마토의 상태값 알려주는 변수 flag 선언
flag = 1
# 상자에 안 익은 토마토가 하나라도 있으면 flag 값 변경
for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            flag = 0
            break
result = 0
# 토마토가 모두 익었다면 날짜 중 최대값 출력
if flag == 1:
    for i in range(m):
        for j in range(n):
            result = max(day[i][j], result)
    print(result)
else:
    print(-1)