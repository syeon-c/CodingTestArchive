import sys


def dfs(row, col):
    # 방문하지 않았을 경우 방문 True 변경
    if not visited[row][col]:
        visited[row][col] = True
        # 집이 있을 경우
        if map_list[row][col] == 1:
            complex_list[cnt - 1] += 1
            # 오른쪽 방문 가능여부 확인
            if (col < n - 1) and not visited[row][col + 1]:
                dfs(row, col + 1)
            # 왼쪽 방문 가능 여부 확인
            if (col > 0) and not visited[row][col - 1]:
                dfs(row, col - 1)
            # 아래쪽 방문 가능 여부 확인
            if (row < n - 1) and not visited[row + 1][col]:
                dfs(row + 1, col)
            # 위쪽 방문 가능 여부 확인
            if (row > 0) and not visited[row - 1][col]:
                dfs(row - 1, col)


# 단지 크기 입력(n*n)
n = int(sys.stdin.readline())
# 단지 지도 입력
map_list = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
# 방문 여부 확인
visited = [[False] * n for _ in range(n)]
# cnt 는 단지의 총 개수, complex_list 는 단지 정보를 담은 리스트
cnt = 0
complex_list = []
# 전체 단지 순회하면서 탐색
for i in range(n):
    for j in range(n):
        if not visited[i][j] and map_list[i][j] == 1:
            complex_list.append(0)
            cnt += 1
        dfs(i, j)

# cnt 출력, complex_list 오름차순 정렬 후 출력
print(cnt)
complex_list.sort()
for i in range(len(complex_list)):
    print(complex_list[i])
