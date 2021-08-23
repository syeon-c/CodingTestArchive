import math


def makeTwo(str):
    str = str.upper()
    strList = []
    for i in range(len(str) - 1):
        tmp = str[i:i + 2]
        if tmp.isalpha():
            strList.append(str[i:i + 2])
    return strList


def solution(str1, str2):
    answer = 0
    # 다중집합 만들기
    str1 = makeTwo(str1)
    str2 = makeTwo(str2)

    # 공집합 예외처리
    if len(str1) == 0 and len(str2) == 0:
        return 65536

    print(str1)
    print(str2)

    str1_copy = str1.copy()
    str2_copy = str2.copy()

    # 교집합
    intersection = []
    for i in str1:
        if i in str2_copy:
            intersection.append(i)
            str2_copy.remove(i)
            str1_copy.remove(i)

    print(intersection)

    # 합집합
    union = intersection + str1_copy + str2_copy
    print(union)
    # 계산
    answer = math.floor((len(intersection) / len(union)) * 65536)

    return answer


str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))
