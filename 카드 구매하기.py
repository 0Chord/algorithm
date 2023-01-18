N = int(input().rstrip())

card_pack_arr = list(map(int, input().rstrip().split()))
card_pack_arr.insert(0, 0)
memo = [0] * 1001
memo[1] = card_pack_arr[1]
for idx in range(2, N + 1):
    memo[idx] = card_pack_arr[idx]
    for col in range(1, idx):
        memo[idx] = max(memo[idx], memo[idx - col] + card_pack_arr[col])

print(memo[N])
