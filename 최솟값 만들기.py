def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    first = 0
    second = 0
    for idx in range(len(A)):
        first += A[idx] * B[idx]
    A.sort(reverse=True)
    B.sort()
    for idx in range(len(A)):
        second += A[idx] * B[idx]

    return min(first, second)
