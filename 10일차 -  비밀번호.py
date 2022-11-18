for t in range(1, 11):
    n, str_number = input().split()
    n = int(n)
    arr = list(map(int, list(str_number)))
    while True:
        flag = True
        for idx in range(len(arr) - 1):
            if arr[idx] == arr[idx + 1]:
                flag = False
                arr[idx] = -1
                arr[idx + 1] = -1

        while True:
            if -1 in arr:
                arr.remove(-1)
            if -1 not in arr:
                break
        if flag:
            break
    result = ""
    for el in arr:
        result += str(el)
    print("#" + str(t), result)
