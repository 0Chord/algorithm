def solution(k, tangerine):
    d = dict()
    for i in range(len(tangerine)):
        try:
            d[str(tangerine[i])] += 1
        except:
            d[str(tangerine[i])] = 1
    arr = list(d.items())
    for i in range(len(arr)):
        arr[i] = list(arr[i])
        arr[i][0] = int(arr[i][0])
    arr.sort(key=lambda x: (-x[1], -x[0]))

    answer = 0

    for i in range(len(arr)):
        if k <= 0:
            return answer
        else:
            answer += 1
            k -= arr[i][1]

    return answer
