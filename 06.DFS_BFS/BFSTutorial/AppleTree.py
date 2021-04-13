from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
sum = 0
q = deque()
# 사과나무의 정가운데 요소를 시작점으로 설정
check[n//2][n//2] = 1
sum += tree[n//2][n//2]
q.append((n//2, n//2))
# 트리의 층 표시
level = 0

# bfs
while q:
    # 탐색 범위의 끝에 도달하면 break
    if level == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        # 현재 위치에서 좌하우상 탐색
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            # 아직 방문하지 않았으면 sum값에 더해주고, 방문 표시, 큐에 추가
            if check[x][y] == 0:
                sum += tree[x][y]
                check[x][y] = 1
                q.append((x, y))
    # 트리 레벨 +1
    level += 1
    print(level, size)
    for x in check:
        print(x)
print(sum)