def solution(orderAmount, taxFreeAmount, serviceFree):

    if serviceFree == 0:
        provideCost = orderAmount
    else:
        provideCost = orderAmount + serviceFree

    if provideCost - taxFreeAmount == 1:
        answer = 0

    answer = (provideCost - taxFreeAmount) / 11

    return answer
