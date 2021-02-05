n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
result = 0


# 0 -> 1 / 1 -> 0 으로 변경
def swap(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


# 변경한 A행렬의 값이 주어진 B행렬과 같은지 검
def isEqual():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return 0
    return 1

# 3*3 행렬의 왼쪽 상단 첫 번째 지점을 기준으로 설정
for i in range(0, n - 2):
    for j in range(0, m - 2):
        # 각 행렬의 같은 위치에 있는 요소의 값이 다르면 swap
        if a[i][j] != b[i][j]:
            swap(i, j)
            result += 1

if isEqual():
    print(result)
else:
    print(-1)
