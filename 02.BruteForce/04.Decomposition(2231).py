n = int(input())

for i in range(1, n+1):
    # i의 각 자릿수의 합 구하는 식
    x = sum(map(int, str(i)))
    const = i + x
    if const == n:
        print(i)
        break
    if i == n:
        print(0)