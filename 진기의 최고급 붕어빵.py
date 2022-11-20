T = int(input().rstrip())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    time = arr[0]
    flag = True
    count = (time // M) * K
    people_count = 1
    if count < people_count:
        flag = False

    for idx in range(1, N):
        people_count += 1
        if count < people_count:
            flag = False
            break

        time += arr[idx]
        count = (time // M) * K

    if flag:
        print("#" + str(t), "Possible")
    else:
        print("#" + str(t), "Impossible")
