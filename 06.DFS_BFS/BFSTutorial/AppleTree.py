from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
res = 0
q = deque()
check[n//2][n//2] = 1
sum += tree[n//2][n//2]
q.append((n//2, n//2))
level = 0
while q:
    if level == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y] == 0:
                sum += tree[x][y]
                check[x][y] = 1
                q.append((x, y))
    level += 1
    print(level, size)
    for x in check:
        print(x)