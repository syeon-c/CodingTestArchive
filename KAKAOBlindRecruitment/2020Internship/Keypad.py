def getDistance(now, target):
    target_position = keypad[target]
    distance = abs(now[0] - target_position[0]) + abs(now[1] - target_position[1])
    return distance


def solution(numbers, hand):
    lnow = [3, 0]
    rnow = [3, 2]
    answer = ''

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lnow = keypad[n]

        elif n in [3, 6, 9]:
            answer += 'R'
            rnow = keypad[n]

        else:
            if getDistance(lnow, n) < getDistance(rnow, n):
                answer += 'L'
                lnow = keypad[n]

            elif getDistance(lnow, n) == getDistance(rnow, n):
                if hand == 'right':
                    answer += 'R'
                    rnow = keypad[n]
                elif hand == 'left':
                    answer += 'L'
                    lnow = keypad[n]

            else:
                answer += 'R'
                rnow = keypad[n]

    return answer


keypad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))
