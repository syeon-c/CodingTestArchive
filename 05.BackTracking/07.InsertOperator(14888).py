from collections import deque
import sys

def func(cnt):
    global max_res, min_res


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

func(0)

print(max_res)
print(min_res)
