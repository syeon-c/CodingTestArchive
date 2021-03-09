import sys


def bfs(map_list, row, col, N, M, visit_list):
    # 배추가 없을 경우 방문 표시 해주고 함수 넘김
    if map_list[row][col] == 0:
        visit_list.append([row, col])
        return [0, visit_list]
    # block 은 인접해 있는 배추 그룹 정보를 담은 리스트, 함수 안에서만 사용
    block = []
    queue = [[row, col]]

    while queue:
        [row, col] = queue.pop(0)
        block.append([row, col])
        visit_list.append([row, col])

        if map_list[row][col] == 1:
            # 아래쪽, 위쪽, 오른쪽, 왼쪽에 배추가 있으면 큐에 추가
            if row < N - 1 and map_list[row + 1][col] == 1 \
                    and [row + 1, col] not in block and [row + 1, col] not in queue:
                queue.append([row + 1, col])
            if row > 0 and map_list[row - 1][col] == 1 \
                    and [row - 1, col] not in block and [row - 1, col] not in queue:
                queue.append([row - 1, col])
            if col < M - 1 and map_list[row][col + 1] == 1 \
                    and [row, col + 1] not in block and [row, col + 1] not in queue:
                queue.append([row, col + 1])
            if col > 0 and map_list[row][col - 1] == 1 \
                    and [row, col - 1] not in block and [row, col - 1] not in queue:
                queue.append([row, col - 1])
    return [len(block), visited]


case = int(sys.stdin.readline())
result = []

for _ in range(case):
    n, m, k = map(int, sys.stdin.readline().split())

    # 배추밭의 정보 리스트화
    mapList = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        mapList[a][b] = 1

    visited = []
    res = 0

    for i in range(n):
        for j in range(m):
            if [i, j] not in visited:
                [size, visited] = bfs(mapList, i, j, n, m, visited)
                # 배추가 있는 경우에만
                if size != 0:
                    res += 1
    result.append(res)

for i in result:
    print(i)
