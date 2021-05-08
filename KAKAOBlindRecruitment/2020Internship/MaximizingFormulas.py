def calc(operation, i, exp):
    if exp.isdigit():  # 더이상 exp에 연산자가 없으면
        return str(exp)  # 숫자를 그대로 리턴

    else:  # operation의 현 순위 연산자에 따라 진행
        if operation[i] == "*":
            exp_split = exp.split("*")  # 연산자로 쪼개고
            temp = []
            for e in exp_split:  # 쪼개진 각 부분에 대해 재귀 실행
                temp.append(calc(operation, i + 1, e))
            return str(eval("*".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수 실행

        if operation[i] == "+":
            exp_split = exp.split("+")
            temp = []
            for e in exp_split:
                temp.append(calc(operation, i + 1, e))
            return str(eval("+".join(temp)))

        if operation[i] == "-":
            exp_split = exp.split("-")
            temp = []
            for e in exp_split:
                temp.append(calc(operation, i + 1, e))
            return str(eval("-".join(temp)))


def solution(expression):
    answer = 0
    priority = [
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*'),
    ]
    for prior in priority:
        result = abs(int(calc(prior, 0, expression)))

        if result > answer:
            answer = result

    return answer


expression = "100-200*300-500+20"
print(solution(expression))