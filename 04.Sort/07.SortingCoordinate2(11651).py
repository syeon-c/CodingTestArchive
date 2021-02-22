import sys
n = int(sys.stdin.readline())
coordinates = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

coordinates.sort(key=lambda num: (num[1], num[0]))

for num in coordinates:
    print(num[0], num[1])