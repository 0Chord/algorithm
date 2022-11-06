T = int(input())

for i in range(1, T + 1):
    num = input()
    arr = list(map(int, input().split()))
    num_arr = [0 for _ in range(101)]

    for el in arr:
        num_arr[el] += 1

    max_num = 0
    idx = 0
    for el in range(len(num_arr)):
        if max_num <= num_arr[el]:
            max_num = num_arr[el]
            idx = el

    print("#" + num, idx)
