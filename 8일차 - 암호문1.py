for t in range(1, 11):
    N = int(input().rstrip())
    bcrypt_arr = list(input().split())
    count = int(input().rstrip())
    command_arr = list(input().split())
    basket_arr = []
    x = 0
    y = 0
    for idx in range(len(command_arr)):
        if command_arr[idx] == "I":
            if basket_arr:
                for index in range(y):
                    bcrypt_arr.insert(x + index, basket_arr[index])
            basket_arr = []
            x = 0
            y = 0
        elif command_arr[idx - 1] == "I":
            x = int(command_arr[idx])
        elif y == 0:
            y = int(command_arr[idx])
        elif y != 0:
            basket_arr.append(command_arr[idx])

        if idx == len(command_arr) - 1:
            for index in range(y):
                bcrypt_arr.insert(x + index, basket_arr[index])

    print("#" + str(t), *bcrypt_arr[0:10])
