def solution(n, lost, reserve):
    student_class = [1 for _ in range(n)]
    lost.sort()
    reserve.sort()
    for el in lost:
        student_class[el - 1] -= 1
    for el in reserve:
        student_class[el - 1] += 1

    for idx in range(n):
        if idx == 0 and student_class[idx] == 2 and student_class[idx + 1] == 0:
            student_class[idx] = 1
            student_class[idx + 1] += 1
        elif idx != 0 and idx != n - 1 and student_class[idx] == 2:
            if student_class[idx - 1] == 0:
                student_class[idx] = 1
                student_class[idx - 1] += 1
            elif student_class[idx + 1] == 0:
                student_class[idx] = 1
                student_class[idx + 1] += 1
        elif idx == n - 1 and student_class[idx] == 2 and student_class[idx - 1] == 0:
            student_class[idx] = 1
            student_class[idx - 1] += 1
    answer = 0
    for el in student_class:
        if el != 0:
            answer += 1
    return answer
