import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().rstrip().split())

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    word_list = ['a', 'n', 't', 'c', 'i']
    arr = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

    another_word_list = []
    for i in range(26):
        if chr(i + 97) not in word_list:
            another_word_list.append(chr(i + 97))

    res = 0
    combs = combinations(another_word_list, k - 5)
    for comb in combs:
        cnt = 0
        for word in arr:
            for char in word:
                if char not in comb and char not in word_list:
                    break
            else:
                cnt += 1
        res = max(res, cnt)

    print(res)
