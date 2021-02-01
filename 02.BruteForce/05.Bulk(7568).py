n = int(input())
whList = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if (whList[i][0] < whList[j][0]) and (whList[i][1] < whList[j][1]):
            rank += 1
    print(rank, end=" ")
