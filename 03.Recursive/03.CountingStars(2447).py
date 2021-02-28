n = int(input())


def printStar(num, x, y):
    if ((x // num) % 3 == 1) and ((y // num) % 3 == 1):
        print(" ", end="")
    else:
        if (num // 3) == 0:
            print("*", end="")
        else:
            printStar(num // 3, x, y)


for i in range(n):
    for j in range(n):
        printStar(n, i, j)
    print("")