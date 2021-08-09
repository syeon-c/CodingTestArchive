def solution(numbers):
    answer = []
    i = 0
    for i in range(i, len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))

numbers = [2,1,3,4,1]
print(solution(numbers))