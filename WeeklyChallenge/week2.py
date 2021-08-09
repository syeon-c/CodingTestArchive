def solution(scores):
    answer = ''
    average = []
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])

        if tmp.count(scores[i][i]) == 1 and (scores[i][i] == max(tmp) or scores[i][i] == min(tmp)):
            tmp.remove(scores[i][i])

        average.append(sum(tmp) / len(tmp))

    for a in average:
        if a >= 90:
            answer += 'A'
        elif 80 <= a < 90:
            answer += 'B'
        elif 70 <= a < 80:
            answer += 'C'
        elif 50 <= a < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer

scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
          [24, 90, 94, 75, 65]]
print(solution(scores))
