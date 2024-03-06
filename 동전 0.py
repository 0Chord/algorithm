import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coin_arr = []
for _ in range(n):
    coin_arr.append(int(sys.stdin.readline().rstrip()))
coin_arr.sort(reverse=True)
coin_cnt = 0
for el in coin_arr:
    if el <= k:
        coin_cnt += k // el
        k -= el * (k // el)
print(coin_cnt)
