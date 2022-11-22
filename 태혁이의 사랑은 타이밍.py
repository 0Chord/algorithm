T = int(input().rstrip())

for t in range(1, T + 1):
    D, H, M = map(int, input().split())
    wating_time = 0
    input_time = 0
    wating_time += D * 24 * 60
    wating_time += H * 60
    wating_time += M
    input_time += 11 * 24 * 60
    input_time += 11 * 60
    input_time += 11

    if wating_time >= input_time:
        print("#" + str(t), wating_time - input_time)
    else:
        print("#" + str(t), -1)
