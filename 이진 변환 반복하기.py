def solution(s):
    s_change = ""
    zero_cnt = 0
    change_cnt = 0

    while True:
        if s == "1":
            break
        flag = False
        for el in s:
            if el == "1":
                s_change += "1"
                flag = True
        if flag:
            change_cnt += 1
        zero_cnt += len(s) - len(s_change)
        s_num = len(s_change)
        s_num = bin(s_num)
        s = str(s_num)[2:]
        s_change = ""
    answer = [change_cnt, zero_cnt]
    return answer
