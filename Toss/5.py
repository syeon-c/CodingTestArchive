def solution(fruitWeights, k):
    answer = []
    case = []

    for i in range(len(fruitWeights) - (k - 1)):
        tmp = []
        count = 0
        for _ in range(k):
            tmp.append(fruitWeights[i + count])
            count += 1
        case.append(tmp)

    for c in case:
        answer.append(max(c))

    answer = list(set(answer))
    answer.sort(reverse=True)
    return answer


fruitWeights = [10, 20, 30, 40, 50]
print(solution(fruitWeights, 2))
