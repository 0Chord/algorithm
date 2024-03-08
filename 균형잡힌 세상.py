import sys

while True:
    arr = list(sys.stdin.readline().rstrip())
    small_stack = []
    middle_stack = []
    all_stack = []
    flag = True
    if arr[0] == '.':
        break
    for idx in range(len(arr)):
        if idx == len(arr) - 1 and arr[len(arr) - 1] == '.':
            break
        elif arr[idx] == '(':
            small_stack.append('(')
            all_stack.append('(')
        elif arr[idx] == ')':
            try:
                small_stack.pop()
                bracket = all_stack.pop()
                if bracket != '(':
                    flag = False
                    break
            except IndexError:
                flag = False
                break
        elif arr[idx] == '[':
            middle_stack.append('[')
            all_stack.append('[')
        elif arr[idx] == ']':
            try:
                middle_stack.pop()
                bracket = all_stack.pop()
                if bracket != '[':
                    flag = False
                    break
            except IndexError:
                flag = False
                break
    if flag and not small_stack and not middle_stack:
        print("yes")
    else:
        print("no")
