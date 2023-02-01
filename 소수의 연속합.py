import sys

N = int(sys.stdin.readline().rstrip())

arr = [i for i in range(1, N + 1)]
prime_arr = [True] * (N + 1)
memo = []
for idx in range(1, len(arr)):
    if prime_arr[idx + 1]:
        memo.append(arr[idx])
        for j in range(idx + 1, N + 1, idx + 1):
            prime_arr[j] = False

result_count = 0

left, right = 0, 0
sum = 0
while True:
    if sum > N:
        sum -= memo[left]
        left += 1
    elif sum == N:
        result_count += 1
        sum -= memo[left]
        left += 1
    elif right == len(memo):
        break
    else:
        sum += memo[right]
        right += 1

print(result_count)
