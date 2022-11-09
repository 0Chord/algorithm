T = int(input().strip())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop()
    del arr[0]
    average_sum = 0
    for el in arr:
        average_sum += el
    average_sum = round(average_sum / 8)
    print("#" + str(t), average_sum)
