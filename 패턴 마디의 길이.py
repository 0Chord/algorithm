T = int(input())

for t in range(1, T + 1):
    pattern_str = input()
    count = 0
    for i in range(1, 11):
        if pattern_str[0:i] == pattern_str[i: 2 * i]:
            count = i
            break
    print("#" + str(t), count)
