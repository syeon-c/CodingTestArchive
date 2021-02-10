n = int(input())
result = 666
count = 0
# 666 1666 2666 3666 4666 5666 6660
# 6661 6662 6663 6664 6665 6667 6668 6669...
# 7666 8666 9666 10666 11666 12666 13666 14666...

while True:
    if '666' in str(result):
        count += 1
    if count == n:
        print(result)
        break
    result += 1
