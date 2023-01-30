arr = list(input())
count = 0
stack = []
for idx in range(len(arr)):
    if arr[idx] == '(' and arr[idx + 1] != ')':
        stack.append(1)
    elif arr[idx] == ')' and arr[idx - 1] == '(':
        for i in range(len(stack)):
            stack[i] += 1
    elif arr[idx] == ')' and arr[idx - 1] != '(':
        count += stack.pop()
print(count)
