import sys


def check_horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True


def check_vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True


def check_bythree(x, y, val):
    # 0-1 / 3-5 / 6-8 세 구역으로 나눔
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx + i][ny + j]:
                return False
    return True


def dfs(cnt):
    # zero 리스트의 요소 모두 접근하면 결과값 출력
    if cnt == len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=' ')
            print()
        sys.exit(0)

    else:
        # i(1-9)가 있는지 확인
        for i in range(1, 10):
            x = zeros[cnt][0]
            y = zeros[cnt][1]
            # 가로, 세로, 3x3 에 i가 없으면 해당 위치에 i 저장, cnt + 1 로 다시 탐색
            if check_horizontal(x, i) and check_vertical(y, i) and check_bythree(x, y, i):
                sudoku[x][y] = i
                dfs(cnt + 1)
                sudoku[x][y] = 0


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# sudoku 리스트에서 0인 요소의 위치 리스트 생성
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)
