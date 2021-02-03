n = int(input())
cards = [int(input()) for _ in range(n)]

cards.sort()
if n == 1:
    result = 0
else:
    result = cards[0] + cards[1]
    for i in range(2, len(cards)):
        result += result + cards[i]

print(result)
