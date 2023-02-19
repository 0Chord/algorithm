import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

incresed_memo = [1] * n
decresed_memo = [0] * n
for idx in range(1, n):
    for j in range(idx):
        if arr[idx] > arr[j]:
            incresed_memo[idx] = max(incresed_memo[idx], incresed_memo[j] + 1)
reversed_arr = list(reversed(arr))
for idx in range(1, n):
    for j in range(idx):
        if reversed_arr[idx] > reversed_arr[j]:
            decresed_memo[idx] = max(decresed_memo[idx], decresed_memo[j] + 1)
result_memo = [0] * n

for idx in range(n):
    result_memo[idx] = incresed_memo[idx] + decresed_memo[n - idx - 1]
print(max(result_memo))