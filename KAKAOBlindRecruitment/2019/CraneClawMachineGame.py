def solution(board, moves):
    answer = 0
    res = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                doll = board[j][i-1]
                if len(res) > 0 and doll == res[-1]:
                    res.pop()
                    answer += 2
                else:
                    res.append(doll)
                board[j][i-1] = 0

    return answer


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
