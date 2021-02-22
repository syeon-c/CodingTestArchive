import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(n))
nums.sort()


def avgSum(list):
    return round(sum(list) / n)


def getMid(list):
    if n == 1:
        return list[0]
    else:
        if n % 2 != 0:
            return list[n // 2]
        else:
            return round((list[n // 2] + list[n // 2 + 1]) / 2)


def manyVal(list):
    if n == 1:
        return list[0]
    val = Counter(list).most_common(2)
    if val[0][1] == val[1][1]:
        return val[1][0]
    else:
        return val[0][0]


def getMin(list):
    return list[n-1]-list[0]

print(avgSum(nums))
print(getMid(nums))
print(manyVal(nums))
print(getMin(nums))
