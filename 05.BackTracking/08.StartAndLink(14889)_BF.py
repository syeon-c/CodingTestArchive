import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def getAbility(team_list):
    sum = 0
    for i in range(len(team_list) - 1):
        for j in range(i + 1, len(team_list)):
            sum += matrix[team_list[i]][team_list[j]] + matrix[team_list[j]][team_list[i]]
    return sum


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
team = deque(combinations(members, n // 2))
min_res = sys.maxsize

start = deque()
link = deque()

for _ in range(len(team) // 2):
    start.append(team.popleft())
    link.append(team.pop())
    print(start)
    print(link)

for i in range(n // 2):
    res = abs(getAbility(start[i]) - getAbility(link[i]))
    if min_res > res:
        min_res = res

print(min_res)
