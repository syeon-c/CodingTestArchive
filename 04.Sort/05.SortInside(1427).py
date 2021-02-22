nums = input()
nums = [int(n) for n in nums]

nums.sort(reverse=True)

for n in nums:
    print(n, end="")
