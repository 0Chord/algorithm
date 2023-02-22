import sys

a, p = map(int, sys.stdin.readline().rstrip().split())

memo = [a]
idx = 0
find_idx = -1
while True:
    calc = 0
    string = str(memo[idx])
    for el in string:
        calc += pow(int(el), p)

    if calc in memo:
        print(memo.index(calc))
        break
    memo.append(calc)
    idx += 1
