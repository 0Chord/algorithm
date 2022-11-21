T = int(input().rstrip())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    divided_arr = [0 for _ in range(101)]
    for el in arr:
        divided_arr[el] += 1
    for idx in range(len(divided_arr)):
        if divided_arr[idx] == 1 or divided_arr[idx] == 3:
            print("#" + str(t), idx)

