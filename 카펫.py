def solution(brown, yellow):
    answer = []
    for idx in range(1, yellow + 1):
        if yellow % idx == 0:
            if idx > yellow // idx:
                break
            if ((yellow // idx) + 2) * 2 + idx * 2 == brown:
                answer.append([yellow // idx + 2, idx + 2])
                break
    return answer[0]
