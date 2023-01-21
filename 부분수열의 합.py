N, S = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

count = 0


def recur(idx, calc):
    global count

    if idx == N:
        return
    calc += arr[idx]
    if calc == S:
        count += 1

    recur(idx + 1, calc)
    recur(idx + 1, calc - arr[idx])


recur(0, 0)
print(count)
