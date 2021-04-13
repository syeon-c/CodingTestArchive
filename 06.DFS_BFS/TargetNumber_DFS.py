def dfs(i, numbers, target, res):
    global answer
    if i == len(numbers) and res == target:
        answer += 1
        return
    elif i == len(numbers):
        return

    dfs(i + 1, numbers, target, res + numbers[i])
    dfs(i + 1, numbers, target, res - numbers[i])


def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, target, 0)
    return answer


numbers = [1, 1, 1]
target = 1
print(solution(numbers, target))