import sys
n = int(sys.stdin.readline())
memberList = []

for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    memberList.append((age, name))

memberList.sort(key=lambda member: (member[0]))

for member in memberList:
    print(member[0], member[1])