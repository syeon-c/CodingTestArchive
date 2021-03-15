import sys


def dfs(cnt):
    global res
    # 팀 분배가 모두 이루어지면 팀의 능력치 계산,능력치의 차이값 중 최소값 비교
    if cnt == (n // 2):
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                # team 리스트의 요소가 1이면 그 인덱스 값에 대응하는 matrix 의 능력치값 start 에 더해줌
                if team[i] and team[j]:
                    start += matrix[i][j]
                # 0이면 그 인덱스 값에 대응하는 matrix의 능력값 link에 더해줌
                elif not team[i] and not team[j]:
                    link += matrix[i][j]
        # res 와 start - link 차이값 비교 후 최소값 res 저장
        res = min(res, abs(start - link))

    for i in range(cnt, n):
        if team[i]:
            continue
        team[i] = 1
        dfs(cnt + 1)
        team[i] = 0


# n은 경기에 참여하는 사람의 수, matrix는 팀 조합 별 능력치 정보를 담은 리스트
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 팀 분배 정보 담을 team 리스트 생성, 0 또는 1로 구성되어 있으며 1은 스타트팀, 0은 링크
team = [0 for _ in range(n)]
res = sys.maxsize

dfs(0)

print(res)
