n = int(input())
nums = [int(input()) for _ in range(n)]

positive = []
negative = []

result = 0
for n in nums:
    if n <= 0:
        negative.append(n)
    elif n == 1:
        result += 1
    elif n > 0:
        positive.append(n)

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        result += positive[i] * positive[i+1]
    else:
        result += positive[i]

for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        result += negative[i] * negative[i+1]
    else:
        result += negative[i]

print(result)