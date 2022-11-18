for t in range(1, 11):
    length = int(input().rstrip())
    arr = input().split()
    count = int(input().rstrip())
    command_arr = input().split()

    for idx in range(len(command_arr)):
        if command_arr[idx] == "I":
            x = int(command_arr[idx + 1])
            y = int(command_arr[idx + 2])
            mini_arr = []
            for index in range(y):
                arr.insert(x + index, command_arr[idx + 3 + index])
        elif command_arr[idx] == "D":
            x = int(command_arr[idx + 1])
            y = int(command_arr[idx + 2])
            del arr[x:x + y]
        elif command_arr[idx] == "A":
            y = int(command_arr[idx + 1])
            for index in range(y):
                arr.append(command_arr[idx + 2 + index])
    print("#" + str(t), *arr[0:10])
