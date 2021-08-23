def possible():
    return True


m, n = map(int, input().split())

day = 0
count = 0

while (day):
    keyword = str(input())

    if keyword == "SHOW":
        if possible():
            print(1)
        else:
            print(0)

    if keyword == "NEGATIVE":
        print(0)

    if keyword == "NEXT":
        print("-")

    if keyword == "EXIT":
        print("BYE")
        break
