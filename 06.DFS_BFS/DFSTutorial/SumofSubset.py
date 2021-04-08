import sys


def dfs(i, sum):
    if i == n:
        # 다른 부분집합의 합과 같을 경우
        if sum == (total - sum):
            print(sum, end=' ')
            print("YES")
            sys.exit(0)
    else:
        dfs(i + 1, sum + a[i])
        dfs(i + 1, sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)
dfs(0, 0)
print("NO")