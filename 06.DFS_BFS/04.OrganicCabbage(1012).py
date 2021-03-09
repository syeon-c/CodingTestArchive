import sys


def dfs(row, col):
    # 방문하지 않았을 경우 방문 True 변경
    if not visited[row][col]:
        visited[row][col] = True
        # 배추가 있을 경우
        if map_list[row][col] == 1:
            # 오른쪽에 배추 있는지 확인
            if (col < m - 1) and not visited[row][col + 1]:
                dfs(row, col + 1)
            # 왼쪽에 배추 있는지 확인
            if (col > 0) and not visited[row][col - 1]:
                dfs(row, col - 1)
            # 아래쪽에 배추 있는지 확인
            if (row < n - 1) and not visited[row + 1][col]:
                dfs(row + 1, col)
            # 위쪽에 배추 있는지 확인
            if (row > 0) and not visited[row - 1][col]:
                dfs(row - 1, col)


# case 는 테스트 케이스의 개수
case = int(sys.stdin.readline())
# result 는 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수 정보를 담은 리스트
result = []


for _ in range(case):
    # n 은 배추밭의 세로 길이, m 은 배추밭의 가로 길이, k 는 배추가 심어져 있는 위치의 개수
    n, m, k = map(int, sys.stdin.readline().split())
    # map_list 는 배추밭의 정보, 배추가 위치한 정보를 입력 받아서 map_list 에 위치 설정
    map_list = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        map_list[x][y] = 1
    # 방문 여부 확인
    visited = [[False] * m for _ in range(n)]
    # result 리스트에 저장할 각각의 케이스에 필요한 배추흰지렁이의 수
    res = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and map_list[i][j] == 1:
                res += 1
                dfs(i, j)
    result.append(res)

for i in result:
    print(i)
