T = int(input())
for i in range(T):
    N = int(input())
    arr = map(int, input().split())

    sum_calc = 0
    max_num = arr[-1]
    for el in reversed(range(len(arr))):
        if max_num > arr[el]:
            sum_calc += (max_num - arr[el])

        if max_num < arr[el]:
            max_num = arr[el]

    print("#", str(i + 1), sum_calc)
