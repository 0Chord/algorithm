T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = list(map(int, input().split()))
    average_salary = 0
    for el in arr:
        average_salary += el
    average_salary /= N
    count = 0
    for el in arr:
        if el <= average_salary:
            count += 1
    print("#" + str(t), count)
