T = int(input().rstrip())

for t in range(1, T + 1):
    n = input().rstrip()
    num = n[-1]
    if int(num) % 2 == 0:
        print("#" + str(t), "Even")
    else:
        print("#" + str(t), "Odd")
