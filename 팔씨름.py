T = int(input().rstrip())

for t in range(1, T + 1):
    arr = list(input().rstrip())
    flag = True
    if len(arr) >= 8:
        x_count = 0
        for el in arr:
            if el == "x":
                x_count += 1
        if x_count >= 8:
            flag = False

    if flag:
        print("#" + str(t), "YES")
    else:
        print("#" + str(t), "NO")
