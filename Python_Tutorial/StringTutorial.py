# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성
def solution(s):
    answer = False

    if len(s) in (4, 6) and s.isdigit():
        answer = True

    return answer


s = "a234"
print(solution(s))
