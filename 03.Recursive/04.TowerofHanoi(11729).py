n = int(input())
moveList = []


def setTower(n, one, two, thr):
    if n == 1:
        moveList.append([one, thr])
        return
    setTower(n - 1, one, thr, two)
    moveList.append([one, thr])
    setTower(n - 1, two, one, thr)


setTower(n, 1, 2, 3)

print(len(moveList))
print("\n".join([' '.join(str(i) for i in row) for row in moveList]))
