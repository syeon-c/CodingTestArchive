import sys

t = int(input())

for _ in range(t):
    n = int(input())
    applicant = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    applicant.sort()

    min = applicant[0][1]
    result = 1

    for a in range(1, len(applicant)):
        if min > applicant[a][1]:
            min = applicant[a][1]
            result += 1

    print(result)