def solution(sizes):
    w = []
    h = []
    for el in sizes:
        if el[0] > el[1]:
            w.append(el[0])
            h.append(el[1])
        else:
            h.append(el[0])
            w.append(el[1])
    return max(h)*max(w)