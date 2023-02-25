from collections import deque


def bfs(n, k):
    queue = deque([(n, 0)])
    visited = [False] * 100001
    visited[n] = True
    memo = [-1] * 100001

    while queue:
        current, time = queue.popleft()
        if current == k:
            path = [current]
            i = current
            while memo[i] != -1:
                path.append(memo[i])
                i = memo[i]
            return path[::-1], time

        for nxt in (current - 1, current + 1, current * 2):
            if 0 <= nxt <= 100000 and not visited[nxt]:
                visited[nxt] = True
                memo[nxt] = current  # 경로 저장
                queue.append((nxt, time + 1))


n, k = map(int, input().split())
path, time = bfs(n, k)
print(time)
print(' '.join(map(str, path)))
