import sys

n = int(sys.stdin.readline().rstrip())

idx = 0
cnt = 0

while True:
    if n == 0:
        print(0)
        break
    if cnt >= 1000001:
        print(-1)
        break
    if idx >9876543210:
        print(-1)
        break
    if idx < 10:
        cnt += 1
        idx += 1
        if cnt == n:
            print(idx)
            break
    else:
        str_idx = str(idx)
        flag = True
        for i in range(len(str_idx) - 1):
            if int(str_idx[i]) <= int(str_idx[i + 1]):
                flag = False
                idx = idx // pow(10, len(str_idx) - i - 1)
                idx += 1
                idx *= pow(10, len(str_idx) - i - 1)
                break
        if flag:
            if cnt == n:
                print(idx)
                break
            cnt += 1
            idx += 1