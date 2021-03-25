from itertools import combinations
from bisect import bisect_left


# 주어진 정보 하나씩 탐색하여 모든 경우에 대한 테이블 생성
def make_info_list(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


def solution(info, query):
    answer = []
    # 점수를 제외한 정보를 key, 점수 정보를 value 값으로 해시맵 생성
    info_dict = {}
    for i in info:
        i = i.split()
        cases = make_info_list(i)
        for case in cases:
            if case not in info_dict.keys():
                info_dict[case] = [int(i[4])]
            else:
                info_dict[case].append(int(i[4]))

    # 딕셔너리내 key값 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        target = q[0] + q[2] + q[4] + q[6]
        if target in info_dict.keys():
            answer.append(len(info_dict[target]) - bisect_left(info_dict[target], int(q[7]), lo=0, hi=len(info_dict[target])))
        else:
            answer.append(0)

        print(q)

    print(info_dict)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
