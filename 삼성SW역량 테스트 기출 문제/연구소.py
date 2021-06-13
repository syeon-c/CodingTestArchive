from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
res = 0
Q = deque()

while Q:



