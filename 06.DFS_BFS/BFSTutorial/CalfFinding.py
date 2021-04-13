from collections import deque

MAX = 10000
ch = [0] * (MAX + 1)
distance = [0] * (MAX + 1)
# s는 현수의 위치, e는 송아지의 위치
s, e = map(int, input().split())
# 현수의 시작 위치 방문 표시
ch[s] = 1
Q = deque()
Q.append(s)

while Q:
    now = Q.popleft()
    if now == e:
        break
    # now - 1, now + 1, now + 5 순으로 BFS
    for next in (now - 1, now + 1, now + 5):
        if 0 <= next <= MAX:
            # 아직 방문하지 않았으
            if ch[next] == 0:
                Q.append(next)
                ch[next] = 1
                distance[next] = distance[now] + 1

print(distance)
print(distance[e])
