for t in range(1, 11):
    dump_count = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    while dump_count > 0:
        arr[-1] -= 1
        dump_count -= 1
        arr[0] += 1
        arr.sort()
    print("#" + str(t), (arr[-1] - arr[0]))
