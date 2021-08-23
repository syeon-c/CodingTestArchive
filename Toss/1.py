def solution(orderAmount, taxFreeAmount, serviceFree):
    answer = 0

    taxAmount = answer * 10

    provideAmount = taxAmount + taxFreeAmount
    provideCost = 0
    answer = taxAmount * 0.1

    if serviceFree == 0:
        provideCost = orderAmount
    else:
        provideCost = orderAmount + serviceFree

    if provideCost - taxFreeAmount == 1:
        answer = 0

    return answer
