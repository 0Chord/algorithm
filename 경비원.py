import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
store = int(sys.stdin.readline().rstrip())
store_arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(store)]
caps_dist = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
#   1북 2남 3서 4동
for el in store_arr:
    if caps_dist[0] == 1:
        if el[0] == 1:
            res += abs(caps_dist[1] - el[1])
        elif el[0] == 2:
            res += min(caps_dist[1] + n + el[1], m - caps_dist[1] + n + m - el[1])
        elif el[0] == 3:
            res += min(caps_dist[1] + el[1], m - caps_dist[1] + m + n + n - el[1])
        elif el[0] == 4:
            res += min(caps_dist[1] + m + n + n - el[1], m - caps_dist[1] + el[1])
            #통과
    elif caps_dist[0] == 2:
        if el[0] == 1:
            res += min(caps_dist[1] + n + el[1], m - caps_dist[1] + n + m - el[1])
        elif el[0] == 2:
            res += abs(caps_dist[1] - el[1])
        elif el[0] == 3:
            res += min(caps_dist[1] + n - el[1], m - caps_dist[1] + n + m + el[1])
        elif el[0] == 4:
            res += min(m - caps_dist[1] + n - el[1], caps_dist[1] + n + m + el[1])
            #통과
    elif caps_dist[0] == 3:
        if el[0] == 1:
            res += min(caps_dist[1] + el[1], n - caps_dist[1] + n + m + m - el[1])
        elif el[0] == 2:
            res += min(n - caps_dist[1] + el[1], caps_dist[1] + m + n + m - el[1])
        elif el[0] == 3:
            res += abs(caps_dist[1] - el[1])
        elif el[0] == 4:
            res += min(caps_dist[1] + m + el[1], n - caps_dist[1] + m + n - el[1])
    elif caps_dist[0] == 4:
        if el[0] == 1:
            res += min(caps_dist[1] + m - el[1], n - caps_dist[1] + m + n + el[1])
        elif el[0] == 2:
            res += min(n - caps_dist[1] + m - el[1], caps_dist[1] + n + m + el[1])
        elif el[0] == 3:
            res += min(caps_dist[1] + m + el[1], n - caps_dist[1] + m + n - el[1])
        elif el[0] == 4:
            res += abs(caps_dist[1] - el[1])
print(res)
