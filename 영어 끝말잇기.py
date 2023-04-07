def solution(n, words):
    arr = []
    answer = [0, 0]
    last_name = ""
    for idx in range(len(words)):
        if idx == 0:
            last_name = words[idx][-1]
            arr.append(words[idx])
        else:
            if words[idx][0] != last_name:
                answer = [idx % n + 1, idx // n + 1]
                break
            elif words[idx] in arr:
                answer = [idx % n + 1, idx // n + 1]
                break
            elif len(words[idx]) == 1:
                answer = [idx % n + 1, idx // n + 1]
                break
            else:
                last_name = words[idx][-1]

    return answer
