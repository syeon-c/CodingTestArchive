def solution(i, score, time):
    global result
    if time > m:
        return
    if i == n:
        if result < score:
            result = score
    else:
        solution(i+1, score + score_list[i], time + time_list[i])
        solution(i+1, score, time)


n, m = map(int, input().split())
score_list = []
time_list = []

result = 0

for i in range(n):
    score, time = map(int, input().split())
    score_list.append(score)
    time_list.append(time)

solution(0, 0, 0)
print(result)