def dfs(i, sum):
    global res
    if i > n:
        if res < sum:
            res = sum
    else:
        if i + T[i] <= n + 1:
            dfs(i + T[i], sum + P[i])
        dfs(i + 1, sum)


n = int(input())

T = [0]
P = [0]
res = -1
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dfs(1, 0)
print(res)