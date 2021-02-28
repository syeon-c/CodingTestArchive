import sys

n = int(sys.stdin.readline())

fib_lambda = lambda n, x=0, y=1: x if n == 0 else fib_lambda(n - 1, y, x + y)

print(fib_lambda(n))
