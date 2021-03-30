def to_binary(x):
    if x == 0: return
    else:
        to_binary(x // 2)
        print(x % 2, end='')


n = int(input())
to_binary(n)