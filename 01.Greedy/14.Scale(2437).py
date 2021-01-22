n = int(input())
nums = list(map(int, input().split()))
nums.sort()

sum = 0
for i in range(n):
    if sum + 1 < nums[i]:
        break
    sum += nums[i]
print(sum + 1)
