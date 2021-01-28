true = [int(input()) for _ in range(9)]
false = []

true.sort()
sumAll = sum(true)

for i in range(len(true) - 1):
    for j in range(i + 1, len(true)):
        a = true[i]
        b = true[j]
        if (a + b) == sumAll - 100:
            false.append(a)
            false.append(b)

true.remove(false[0])
true.remove(false[1])

for i in true:
    print(i)
