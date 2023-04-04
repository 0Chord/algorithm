def solution(s):
    arr = s.split(" ")
    for idx in range(len(arr)):
        arr[idx] = list(arr[idx])
        for i in range(len(arr[idx])):
            if i == 0:
                first = ord(arr[idx][0])
                if 97 <= first <= 122:
                    arr[idx][i] = chr(first-32)
            else:
                if 65<=ord(arr[idx][i])<=90:
                    arr[idx][i] = chr(ord(arr[idx][i])+32)
        arr[idx] = "".join(arr[idx])
    arr = " ".join(arr)
    return arr