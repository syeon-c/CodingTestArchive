def dfs(i, sum):
    global res
    if i == k:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(i+1, sum + grams[i])
        dfs(i+1, sum - grams[i])
        dfs(i+1, sum)

k = int(input())
grams = list(map(int, input().split()))
s = sum(grams)
res = set()
dfs(0, 0)
print(res)
print(s - len(res))