for t in range(1, 11):
    N = int(input().rstrip())
    password_arr = list(input().split())
    command_count = int(input().rstrip())
    command_arr = list(input().split())

    for idx in range(len(command_arr)):
        if command_arr[idx] == "I":
            x = command_arr[idx + 1]
            y = command_arr[idx + 2]
            for index in range(int(y)):
                password_arr.insert(int(x) + index, command_arr[index + idx + 3])
        elif command_arr[idx] == "D":
            x = int(command_arr[idx + 1])
            y = int(command_arr[idx + 2])
            for _ in range(y):
                password_arr.pop(x)

    print("#" + str(t), *password_arr[0:10])
