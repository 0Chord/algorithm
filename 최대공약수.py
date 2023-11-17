import sys
from math import gcd

n = int(sys.stdin.readline().rstrip())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

n_value = 1
m_value = 1

n_arr.sort()
m_arr.sort()

value = 0
for el in n_arr:
    n_value *= el

for m_el in m_arr:
    m_value *= m_el

value = max(value, gcd(n_value, m_value))
result = str(value)
if len(result) > 9:
    print(result[-9:])
else:
    print(result)
