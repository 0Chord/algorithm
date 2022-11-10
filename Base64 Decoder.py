T = int(input().rstrip())

encoding_buffer = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
for t in range(1, T + 1):
    input_str = input().rstrip()
    decoding_buffer = ""
    for idx in range(0, len(input_str), 4):
        buffer = input_str[idx:idx + 4]
        count = ""
        for e in buffer:
            count += bin(encoding_buffer.find(e))[2:].zfill(6)
        for index in range(0, len(count), 8):
            decoding_buffer += chr(int(count[index:index + 8], 2))
    print("#" + str(t), decoding_buffer)
