def dfs(i, score, time):
    global res
    if time > m:
        return
    if i == n:
        if res < score:
            res = score
    else:
        dfs(i + 1, score + p_value[i], time + p_time[i])
        dfs(i + 1, score, time)


# n은 문제의 개수, m은 제한시간
n, m = map(int, input().split())
p_value = []
p_time = []

for i in range(n):
    a, b = map(int, input().split())
    p_value.append(a)
    p_time.append(b)
res = int(-1e9)

dfs(0, 0, 0)
print(res)