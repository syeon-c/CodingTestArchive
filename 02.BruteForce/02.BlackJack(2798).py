n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = cards[0] + cards[1] + cards[2]

for x in range(n - 2):
    for y in range(x + 1, n - 1):
        for z in range(y + 1, n):
            num = cards[x] + cards[y] + cards[z]
            if abs(m - num) < abs(m - result) and num <= m:
                result = num
print(result)
