import sys

n = int(sys.stdin.readline())
nums = [0 for i in range(10000)]

for _ in range(n):
    num = int(sys.stdin.readline())
    nums[num] = nums[num] + 1

for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)