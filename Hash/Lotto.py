# 1부터 45까지의 숫자 중 6개를 찍어서 맞는 복권
# 복권을 맞춘 개수에 따라 순위 존재
# 선택한 6개의 숫자 중 알아보기 힘든 숫자 0 표시
# 선택한 로또 번호 중 당첨 번호 6와 일치 가능한 최고 순위와 최저 순위 출력
def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer = []
    cnt = lottos.count(0)
    win = 0

    for l in lottos:
        if l in win_nums:
            win += 1

    answer.append(rank.get(win + cnt))
    answer.append(rank.get(win))

    return answer