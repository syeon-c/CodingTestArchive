def solution(s):
    answer = ''
    l = len(s)

    if l % 2 == 0:
        answer += s[l // 2 - 1]
        answer += s[l // 2]

    elif l % 2 == 1:
        answer += s[l // 2]

    return answer


s = "abcde"
print(solution(s))
