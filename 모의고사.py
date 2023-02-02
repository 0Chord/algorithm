def solution(answers):
    first = []
    for _ in range(2000):
        for idx in range(1, 6):
            first.append(idx)
    second = []
    for _ in range(1250):
        for idx in range(1, 6):
            if idx != 2:
                second.append(2)
                second.append(idx)
    third = []
    for _ in range(1000):
        for idx in range(1, 6):
            if idx == 1:
                for _ in range(2):
                    third.append(3)
            elif idx == 2 or idx == 3:
                for _ in range(2):
                    third.append(idx - 1)
            else:
                for _ in range(2):
                    third.append(idx)
    first_count = 0
    second_count = 0
    third_count = 0
    for idx in range(len(answers)):
        if first[idx] == answers[idx]:
            first_count += 1
        if second[idx] == answers[idx]:
            second_count += 1
        if third[idx] == answers[idx]:
            third_count += 1
    max_num = max(first_count, second_count, third_count)
    answer = []
    if first_count == max_num:
        answer.append(1)
    if second_count == max_num:
        answer.append(2)
    if third_count == max_num:
        answer.append(3)
    answer.sort()
    return answer
