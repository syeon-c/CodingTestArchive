from collections import Counter
from functools import reduce


def solution(clothes):
    count = Counter([sort for name, sort in clothes])
    print(count)
    answer = reduce(lambda x, y: x*(y+1), count.values(), 1) - 1
    return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))