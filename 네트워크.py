count = 0


def solution(n, computers):
    global count
    arr = [[] for _ in range(n)]
    visited = [False] * n
    for col in range(n):
        for row in range(n):
            if col != row and computers[col][row] == 1:
                arr[col].append(row)

    for idx in range(n):
        if not visited[idx]:
            count += 1
            dfs(idx, arr, visited)
    answer = 0
    return count


def dfs(idx, lst, visited):
    if visited[idx]:
        return
    visited[idx] = True
    for el in lst[idx]:
        dfs(el, lst, visited)
