INF = int(1e10)


def solution(msg):
    word_arr = {}
    for i in range(26):
        word_arr[chr(i + 65)] = (i + 1)
    order = 27
    answer = []
    i = 0
    while True:
        if i == len(msg):
            break
        for j in range(1, INF):
            try:
                if word_arr[msg[i:i + j]]:
                    if i + j == len(msg):
                        answer.append(word_arr[msg[i:i + j]])
                        i += j
                        break
                    continue
            except:
                word_arr[msg[i:i + j]] = order
                order += 1
                answer.append(word_arr[msg[i:i + j - 1]])
                i += j - 1
                break
    return answer
