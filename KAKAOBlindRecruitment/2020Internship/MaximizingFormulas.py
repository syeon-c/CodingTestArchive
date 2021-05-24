def cal(operation, i, exp):
    if exp.isdigit():
        print('digit: ' + str(exp))
        return str(exp)

    else:
        if operation[i] == '*':
            exp_split = exp.split('*')
            tmp = []
            for e in exp_split:
                tmp.append(cal(operation, i + 1, e))
                print(tmp)
            print('*: ' + str(eval('*'.join(tmp))))
            return str(eval('*'.join(tmp)))

        if operation[i] == '+':
            exp_split = exp.split('+')
            tmp = []
            for e in exp_split:
                tmp.append(cal(operation, i + 1, e))
                print(tmp)
            print('+: ' + str(eval('+'.join(tmp))))
            return str(eval('+'.join(tmp)))

        if operation[i] == '-':
            exp_split = exp.split('-')
            tmp = []
            for e in exp_split:
                tmp.append(cal(operation, i + 1, e))
                print(tmp)
            print('-: ' + str(eval('-'.join(tmp))))
            return str(eval('-'.join(tmp)))


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
        print('--------------')
        result = abs(int(cal(prior, 0, expression)))

        if result > answer:
            answer = result

    return answer


expression = "100-200*300-500+20"
print(solution(expression))