def dfs(i, sum):
    global result
    if i > n:
        if result < sum:
            result = sum
    else:
        # 남은 일수를 넘지 않으면
        if i + T[i] <= n + 1:
            dfs(i + T[i], sum + P[i])
        dfs(i + 1, sum)


n = int(input())
T = []
P = []
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
result = -1
# 1-n 이기 때문에 인덱스 0 채워줌
T.insert(0, 0)
P.insert(0, 0)
dfs(1, 0)
print(result)
