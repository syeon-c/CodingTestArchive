def dfs(i, sum):
    global res
    if i == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(i+1, sum + grams[i])
        dfs(i+1, sum - grams[i])
        dfs(i+1, sum)


n = int(input())
grams = list(map(int, input().split()))
s = sum(grams)
# 중복제거를 위해 집합으로 정의
res = set()
dfs(0, 0)
print(s - len(res))