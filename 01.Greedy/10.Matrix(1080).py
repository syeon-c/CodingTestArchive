n, m = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]


def swap(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


def isEqual():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return 0
    return 1


result = 0

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            swap(i, j)
            result += 1

if isEqual():
    print(result)
else:
    print(-1)
