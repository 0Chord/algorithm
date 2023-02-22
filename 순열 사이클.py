import sys
sys.setrecursionlimit(int(1e8))
t = int(sys.stdin.readline().rstrip())


def dfs(start):
    if visited[start]:
        return
    visited[start] = True
    dfs(arr[start])


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [False] * (n + 1)
    cycle_count = 0
    for idx in range(1,n+1):
        if not visited[idx]:
            cycle_count += 1
            dfs(idx)
    print(cycle_count)
