import math

T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(input().rstrip()))
    shop_count = 0
    for el in arr:
        for e in el:
            if e == "#":
                shop_count += 1
    if shop_count == 1:
        print("#" + str(t), "yes")
    elif math.sqrt(shop_count) - int(math.sqrt(shop_count)) != 0:
        print("#" + str(t), "no")
    else:
        flag = False
        for col in range(N - int(math.sqrt(shop_count)) + 1):
            for row in range(N - int(math.sqrt(shop_count)) + 1):
                count = 0
                for mini_col in range(int(math.sqrt(shop_count))):
                    for mini_row in range(int(math.sqrt(shop_count))):
                        if arr[col + mini_col][row + mini_row] == "#":
                            count += 1
                if count == shop_count:
                    flag = True
        if flag:
            print("#" + str(t), "yes")
        else:
            print("#" + str(t), "no")
