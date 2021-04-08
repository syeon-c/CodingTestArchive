n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]


def process(x, res):
    cost = 0
    # x가 주어진 기간보다 클 경우(퇴사 후)
    if x > n: return 0
    # x가 주어진 기간만큼일 경우 결과 반환
    if x == n: return res
    # 지금까지의 수입과, x의 수익과, 그 다음 요소인 x+1 중 수입이 최대인 값을 cost에 저장
    cost = max(cost, process(x + schedule[x][0], res + schedule[x][1]), process(x + 1, res))
    return cost


print(process(0, 0))
