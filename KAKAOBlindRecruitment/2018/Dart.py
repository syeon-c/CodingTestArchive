def solution(dartResult):
    score = []
    stack = []
    for i in dartResult:
        if i.isdigit():
            if i == "0" and len(score) != 0 and score[-1] == 1:
                score.pop()
                score.append(10)
            else:
                score.append(int(i))

        elif i in ["S", "D", "T"]:
            if i == "S":
                score[-1] = score[-1] ** 1

            elif i == "D":
                score[-1] = score[-1] ** 2

            elif i == "T":
                score[-1] = score[-1] ** 3

        elif i in ["*", "#"]:
            if i == "*":
                if len(score) > 1:
                    score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            elif i == "#":
                score[-1] = score[-1] * (-1)

    return sum(score)


dartResult = "1S*2T*3S"
print(solution(dartResult))
