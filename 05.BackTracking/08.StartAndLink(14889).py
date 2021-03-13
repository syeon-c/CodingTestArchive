import sys
from copy import deepcopy


def dfs(cnt):
    global res


n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start = []
link = []
res = float('Inf')
