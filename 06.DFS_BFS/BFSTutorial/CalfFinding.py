from collections import deque

MAX = 10000
ch = [0] * (MAX + 1)
distance = [0] * (MAX + 1)

s, e = map(int, input().split())

ch[s] = 1
Q = deque()
Q.append(s)

while Q:
    now = Q.popleft()
    if now == e:
        break
    for i in range(now - 1, now + 1, now + 5):
        if 0 < i <= MAX:
            if ch[i] == 0:
                Q.append(i)
                ch[i] = 1
                distance[i] = distance[now] + 1

print(distance[e])
