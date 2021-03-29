from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), i)
            temp += combi
        print(temp)
        count = Counter(temp)
        if len(count) != 0 and max(count.values()) > 1:
            for j in count:
                if count[j] == max(count.values()):
                    answer += [''.join(j)]

    return sorted(answer)


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]

print(solution(orders, course))