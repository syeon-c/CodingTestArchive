def dfs(i, sum):
    global res
    if i == k:
        if sum == t:
            res += 1
    else:
        for j in range(N[i] + 1):
            dfs(i + 1, sum + (P[i] * j))


t = int(input())
k = int(input())
P = []
N = []
for _ in range(k):
    p, n = map(int, input().split())
    P.append(p)
    N.append(n)
res = 0
dfs(0, 0)
print(res)
