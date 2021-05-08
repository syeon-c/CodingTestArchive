def isInDict(s, dict):
    if s in dict:
        return True
    else:
        return False


def solution(s):
    answer = 0
    answer_string = ''
    temp = ''
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in s:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer_string += i
        else:
            temp += i
            if isInDict(temp, dict):
                answer_string += str(dict[temp])
                temp = ''

    answer = int(answer_string)

    return answer


s = 'one4seveneight'
print(solution(s))
