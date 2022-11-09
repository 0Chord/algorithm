T = int(input())

for t in range(1, T + 1):
    sample_str = input().strip()
    if len(sample_str) % 2 == 1:
        before_str = sample_str[0:len(sample_str) // 2]
        after_str = sample_str[len(sample_str) // 2 + 1:]
        if before_str[::-1] == after_str:
            print("#" + str(t), 1)
        else:
            print("#" + str(t), 0)
    else:
        before_str = sample_str[0:len(sample_str) // 2]
        after_str = sample_str[len(sample_str) // 2:]
        if before_str[::-1] == after_str:
            print("#" + str(t), 1)
        else:
            print("#" + str(t), 0)
