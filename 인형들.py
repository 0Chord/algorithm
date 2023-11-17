import math
import sys
from decimal import Decimal

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
min_result = 1000000000000000
position_list = []
for idx in range(n - k + 1):
    for j_index in range(idx + k - 1, n):
        position_list.append([idx, j_index])

for el in position_list:
    divided_list = arr[el[0]:el[1] + 1]
    average = sum(divided_list)
    average /= len(divided_list)
    result = 0
    var = sum([(x - average) ** 2 for x in divided_list]) / len(divided_list)
    min_result = min(Decimal(math.sqrt(var)), min_result)

print(min_result)
