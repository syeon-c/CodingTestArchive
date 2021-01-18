# N은 로프의 개수, W는 로프들을 이용하여 들을 수 있는 최대 중량
n = int(input())
lopes = list(int(input()) for _ in range(n))
lopes.sort()

# 임의로 로프 리스트 중 가장 작은 값을 기준으로 한 최대 중량 설정
w = lopes[0]*n

for i in range(1, n):
    x = lopes[i] * (n-1)

    # 임의로 설정된 최대 중량보다 클 경우 값 바꿈
    if x > w:
        w = x
    n -= 1

print(w)