T = int(input().rstrip())


def calories(idx, score, cal):
    global result

    if cal > L:
        return

    if result < score:
        result = score

    if idx == N:
        return

    calories(idx + 1, score + arr[idx][0], cal + arr[idx][1])
    calories(idx + 1, score, cal)


for t in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    result = 0
    calorie = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    calories(0, 0, 0)
    print("#" + str(t), result)
