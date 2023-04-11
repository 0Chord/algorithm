def solution(clothes):
    d = {}
    cnt = 1
    for el in clothes:
        try:
            d[el[1]].append(el[0])
        except:
            d[el[1]] = []
            d[el[1]].append(el[0])
    val = list(d.values())

    for i in range(len(val)):
        val[i] = len(val[i])
        cnt *= (val[i] + 1)

    return cnt - 1
