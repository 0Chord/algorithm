import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
a_dist = 0
b_dist = 0
result = []
while True:
    if a_dist == N or b_dist == M:
        break

    if A[a_dist] < B[b_dist]:
        result.append(A[a_dist])
        a_dist += 1
    elif A[a_dist] > B[b_dist]:
        result.append(B[b_dist])
        b_dist += 1
    else:
        result.append(A[a_dist])
        result.append(B[b_dist])
        a_dist += 1
        b_dist += 1

for idx in range(a_dist, N):
    result.append(A[idx])

for idx in range(b_dist, M):
    result.append(B[idx])

print(*result)