import sys
n = int(sys.stdin.readline())


def factorial_for(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


print(factorial_for(n))
