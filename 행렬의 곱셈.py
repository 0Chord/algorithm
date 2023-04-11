def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for idx in range(len(arr1)):
        for row in range(len(arr2[0])):
            calc = 0
            for col in range(len(arr2)):
                calc += arr1[idx][col] * arr2[col][row]
            answer[idx][row] = calc

    return answer