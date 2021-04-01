def dfs(x):
    if x > n:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=" ")
        print()

    else:
        # 1 이면 해당 값 사용
        check[x] = 1
        dfs(x + 1)
        # 0 이면 해당 값 미사용
        check[x] = 0
        dfs(x + 1)


n = int(input())
check = [0] * (n + 1)
dfs(1)
