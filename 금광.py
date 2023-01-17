T = int(input().rstrip())
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    graph = []
    for idx in range(0, n * m - m + 1, m):
        graph.append(arr[idx:idx + m])
    memo = [[0 for _ in range(m)] for _ in range(n)]
    for idx in range(n):
        memo[idx][0] = graph[idx][0]

    for row in range(1, m):
        for col in range(n):
            if col == 0:
                memo[col][row] = max(memo[col][row - 1] + graph[col][row], memo[col + 1][row - 1] + graph[col][row])
            elif col < n - 1:
                memo[col][row] = max(memo[col][row - 1] + graph[col][row], memo[col - 1][row - 1] + graph[col][row],
                                     memo[col + 1][row - 1] + graph[col][row])
            elif col == n - 1:
                memo[col][row] = max(memo[col][row - 1] + graph[col][row], memo[col - 1][row - 1] + graph[col][row])

    max_num = 0
    for el in memo:
        if max_num < max(el):
            max_num = max(el)
    print(max_num)
