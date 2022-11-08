T = int(input())
encoding_list = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111",
                 "0001011"]
for t in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0
    for _ in range(N):
        count_list = []
        encoding_str = input()
        if "1" in encoding_str:
            idx = 0
            for i in range(M - 1, 0, -1):
                if encoding_str[i] == "1":
                    idx = i
                    break
            result_arr = []
            for i in range(8):
                cut_str = encoding_str[idx - 7 * (i + 1) + 1:idx + 1 - 7 * i]
                for n in range(len(encoding_list)):
                    if encoding_list[n] == cut_str:
                        result_arr.append(n)
            calc = (result_arr[0] + result_arr[2] + result_arr[4] + result_arr[6]) + (
                        result_arr[1] + result_arr[3] + result_arr[5] + result_arr[7]) * 3
            if calc % 10 == 0:
                count = (result_arr[0] + result_arr[1] + result_arr[2] + result_arr[3] + result_arr[4] + result_arr[5] +
                         result_arr[6] + result_arr[7])
            else:
                count = -1
    if count == -1:
        print("#" + str(t), 0)
    else:
        print("#" + str(t), count)
