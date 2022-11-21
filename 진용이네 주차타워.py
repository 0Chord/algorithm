TC = int(input().rstrip())

for t in range(1, TC + 1):
    n, m = map(int, input().split())
    weight_cost_arr = []
    for _ in range(n):
        weight_cost_arr.append(int(input().rstrip()))
    car_weight_arr = []
    for _ in range(m):
        car_weight_arr.append(int(input().rstrip()))
    cost = 0
    arr = [0 for _ in range(n)]
    queue = []
    for _ in range(2 * m):
        idx = int(input().rstrip())
        flag = False
        for i in range(n):
            if arr[i] == 0:
                flag = True
                break
        if flag:
            if idx > 0:
                queue.append(idx)
                for i in range(n):
                    if arr[i] == 0:
                        if not queue:
                            arr[i] = 0
                            break
                        else:
                            pop = queue.pop(0)
                            arr[i] = pop
                            cost += car_weight_arr[pop - 1] * weight_cost_arr[i]
                            break
            else:
                for i in range(n):
                    if arr[i] == abs(idx):
                        arr[i] = 0
                        break
        else:
            if idx > 0:
                queue.append(idx)
            else:
                for i in range(n):
                    if arr[i] == abs(idx):
                        if not queue:
                            arr[i] = 0
                            break
                        else:
                            pop = queue.pop(0)
                            arr[i] = pop
                            cost += car_weight_arr[pop - 1] * weight_cost_arr[i]
                            break

    print("#" + str(t), cost)
