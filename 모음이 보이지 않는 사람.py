T = int(input().rstrip())

for t in range(1, T + 1):
    input_str = list(input().rstrip())
    for idx in range(len(input_str)):
        if input_str[idx] == 'a' or input_str[idx] == 'u' or input_str[idx] == 'o' or input_str[idx] == 'e' or \
                input_str[idx] == 'i':
            input_str[idx] = ''
    print("#" + str(t), ''.join(input_str))
