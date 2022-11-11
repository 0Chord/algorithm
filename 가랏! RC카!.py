T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    distance = 0
    speed = 0
    for el in arr:
        if el[0] == 1:
            speed += el[1]
            distance += speed
        elif el[0] == 2:
            if speed - el[1] < 0:
                speed = 0
            else:
                speed -= el[1]
                distance += speed
        elif el[0] == 0:
            distance += speed
    print("#" + str(t), distance)
