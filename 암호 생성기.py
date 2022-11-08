for t in range(1, 11):
    test_case = input()
    arr = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(len(arr) - 1):
            tmp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = tmp
        count += 1
        arr[-1] -= count
        if count == 5:
            count = 0
        if arr[-1] <= 0:
            break
    arr[-1] = 0
    print("#" + str(t), *arr)
