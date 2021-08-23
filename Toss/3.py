def isThree(text):
    textList = text.split(',')

    for i in range(1, len(textList)):
        if len(textList[i]) != 3:
            return False

    return True


def solution(amountText):
    answer = False

    for a in amountText:
        if a.isdigit() or a == ',':
            answer = True
        else:
            return False

    if amountText[0] == '0':
        answer = False

    if not isThree(amountText):
        answer = False

    return answer


amountText = "25,000"
print(solution(amountText))
