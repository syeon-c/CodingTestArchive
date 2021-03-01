import sys

n = int(sys.stdin.readline())

map_list = [0 for _ in range(n)]
visited = [0 for _ in range(n)]
result = 0


def possible(index, c):
    for i in range(index):
        # 행과 열의 차이가 같은 경우
        if index - i == abs(c - map_list[i]):
            return True
    return False


def dfs(idx):
    if idx == n:
        global result
        result += 1
        return
    for i in range(n):
        # 이미 사용한 열일 경우
        if visited[i]:
            continue
        # 대각선에 해당하는 경우
        if possible(idx, i):
            continue
        visited[i] = 1
        map_list[idx] = i
        dfs(idx + 1)
        visited[i] = 0


dfs(0)
print(result)
