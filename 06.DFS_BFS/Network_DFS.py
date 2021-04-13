def dfs(i, n, computers, check):
    check[i] = 1
    for x in range(n):
        if x != i and computers[i][x] == 1 and check[x] == 0:
            dfs(x, n, computers, check)


def solution(n, computers):
    answer = 0
    check = [0 for _ in range(n)]
    for i in range(n):
        if check[i] == 0:
            answer += 1
            dfs(i, n, computers, check)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))