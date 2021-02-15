n = int(input())
Fibo = []

for i in range(n+1):
    if i == 0:
        Fibo.append(0)
    elif i == 1 or i == 2:
        Fibo.append(1)
    else:
        Fibo.append(Fibo[i-2]+Fibo[i-1])

print(Fibo[n])