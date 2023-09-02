import sys

n, m, k = list(map(int, sys.stdin.readline().rstrip().split()))
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

num_list.sort(reverse=True)

result = 0

first = num_list[0]
second = num_list[1]

first_cnt = m // (k + 1) * k + m % (k + 1)
second_cnt = m // (k + 1)

result += first_cnt*first + second_cnt*second

print(result)

