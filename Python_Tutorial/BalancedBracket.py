import sys
n = int(sys.stdin.readline())

for _ in range(n):
    stack = []
    flag = True
    ps = sys.stdin.readline()

    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()

    if len(stack) == 0 and flag == True:
        print('YES')
    else:
        print('NO')