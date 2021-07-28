def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer = []
    count = 0

    for l in lottos:
        if l != 0:
            if l not in win_nums:
                lottos.remove(l)
        else:
            count += 1

    max = len(lottos)

    answer.append(rank.get(max))
    answer.append(rank.get(max - count))

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))
