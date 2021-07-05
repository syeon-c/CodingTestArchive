def dfs(i, score, time):
    global res
    if time > m:
        return
    if i == n:
        if res < score:
            res = score
    else:
        dfs(i + 1, score + SCORE[i], time + TIME[i])
        dfs(i + 1, score, time)


n, m = map(int, input().split())

SCORE = []
TIME = []
res = int(-1e9)

for _ in range(n):
    score, time = map(int, input().split())
    SCORE.append(score)
    TIME.append(time)

dfs(0, 0, 0)
print(res)