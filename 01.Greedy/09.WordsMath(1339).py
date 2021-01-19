n = int(input())
words = list(input().upper() for _ in range(n))
dict = {}

for word in words:
    n = len(word) - 1
    for i in word:
        if i in dict:
            dict[i] += pow(10, n)
        else:
            dict[i] = pow(10, n)
        n -= 1

result = 0
values = []
for value in dict.values():
    values.append(value)
values.sort(reverse=True)

n = 9
for i in range(0, len(values)):
    values[i] *= n
    result += values[i]
    n -= 1

print(result)
