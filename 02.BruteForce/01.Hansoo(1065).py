n = int(input())
result = 0

if n < 100:
    result += n
elif n >= 100:
    result += 99
    for n in range(100, n+1):
        one = n // 100
        two = (n % 100) // 10
        thr = (n % 100) % 10
        if (one - two) == (two - thr):
            result += 1
print(result)
