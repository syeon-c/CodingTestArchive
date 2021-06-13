def dfs(i, sum, n, T, P):
    global result
    if i > n:
        if result < sum:
            result = sum
    else:
        if i + T[i] <= n + 1:
            dfs(i + T[i], sum + P[i], n, T, P)
        dfs(i+1, sum, n, T, P)


n = int(input())
T = []
P = [[] * n]
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

result = -1
T.insert(0, 0)
P.insert(0, 0)
dfs(1, 0, n, T, P)
print(result)