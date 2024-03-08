import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    ps_arr = list(sys.stdin.readline().rstrip())
    stack = []
    flag = True
    for el in ps_arr:
        if el == '(':
            stack.append('(')
        elif el == ')':
            try:
                stack.pop()
            except IndexError:
                flag = False
                break
    if not stack and flag:
        print("YES")
    else:
        print("NO")
