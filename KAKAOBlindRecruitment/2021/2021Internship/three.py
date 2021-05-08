def printList(list):
    result = ''
    for l in list:
        if l == 1:
            result += 'O'
        else:
            result += 'X'
    return result


def solution(n, k, cmd):
    answer = ''
    p_list = [1 for _ in range(n)]
    temp = []
    for c in cmd:
        print(k)
        if c == 'C':
            p_list[k] = 0
            temp.append(k)
            if k == (n - 1):
                k = k - 1
            else:
                k = k + 1

        elif c == 'Z':
            t = temp.pop()
            p_list[t] = 1

        else:
            if c[0] == 'D':
                for _ in range(int(c[-1])):
                    if p_list[k + 1] == 0:
                        k += 2
                    else: k += 1

            elif c[0] == 'U':
                for _ in range(int(c[-1])):
                    if p_list[k - 1] == 0:
                        k -= 2
                    else: k -= 1

    answer = printList(p_list)

    return answer


n, k = 8, 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
