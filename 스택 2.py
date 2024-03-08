import sys

n = int(sys.stdin.readline().rstrip())
commands = []
for _ in range(n):
    commands.append(list(map(int, sys.stdin.readline().rstrip().split())))

arr = []

for command in commands:
    if command[0] == 1:
        arr.append(command[1])
    elif command[0] == 2:
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(arr))
    elif command[0] == 4:
        if arr:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if arr:
            print(arr[len(arr) - 1])
        else:
            print(-1)
