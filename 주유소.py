import sys

n = int(sys.stdin.readline().rstrip())
dist_arr = list(map(int, sys.stdin.readline().rstrip().split()))
charge_arr = list(map(int, sys.stdin.readline().rstrip().split()))

current_gas_price = charge_arr[0]
result = dist_arr[0] * charge_arr[0]
for idx in range(1, n - 1):
    if current_gas_price * dist_arr[idx] > charge_arr[idx] * dist_arr[idx]:
        result += charge_arr[idx] * dist_arr[idx]
        current_gas_price = charge_arr[idx]
    else:
        result += current_gas_price * dist_arr[idx]

print(result)
