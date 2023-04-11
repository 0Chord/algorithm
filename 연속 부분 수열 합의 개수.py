def solution(elements):
    s = set()
    arr = elements + elements
    for idx in range(1, len(arr)):
        arr[idx] += arr[idx - 1]
    for i in range(1, len(elements) + 1):
        for j in range(i - 1, len(elements) + i):
            if j == i - 1:
                s.add(arr[j])
            else:
                s.add(arr[j] - arr[j - i])
    return len(s)
