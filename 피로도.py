from itertools import permutations


def solution(k, dungeons):
    max_cnt = 0
    for permutation in permutations(dungeons, len(dungeons)):
        n = k
        cnt = 0
        for el in list(permutation):
            if n >= el[0]:
                cnt += 1
                n -= el[1]
            else:
                break
        max_cnt = max(max_cnt, cnt)
    return max_cnt
