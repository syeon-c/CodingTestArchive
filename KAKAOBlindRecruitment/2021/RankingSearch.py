from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    # 점수를 제외한 정보를 key, 점수 정보를 value 값으로 해시맵 생성
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_val = int(i[-1])
        for j in range(len(i)):
            for combi in combinations(info_key, j):
                tmp_key = ''.join(combi)
                info_dict[tmp_key].append(info_val)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)
