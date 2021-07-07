def dfs(i, sum):
    global res
    if i == k:
        if 0 < sum <= s:
           res.add(sum)
    else:
        dfs(i + 1, sum + grams[i])
        dfs(i + 1, sum - grams[i])
        dfs(i + 1, sum)


k = int(input())
grams = list(map(int, input().split()))
# 추의 총 합
s = sum(grams)
# res = 측정 가능한 물의 무게, 중복 제거를 위한 집합 처리
res = set()
dfs(0, 0)
print(s - len(res))