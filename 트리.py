import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
delete_node = int(sys.stdin.readline().rstrip())

node = [[] for _ in range(N)]
for idx in range(len(arr)):
    if arr[idx] != -1:
        node[arr[idx]].append(idx)
for idx in range(len(node)):
    if delete_node in node[idx]:
        for col in range(len(node[idx])):
            if node[idx][col] == delete_node:
                if len(node[idx]) == 1:
                    node[idx] = []
                else:
                    node[idx][col] = -2
                break
queue = deque()
visited_arr = [False] * N
leaf_count = 0
for idx in range(len(arr)):
    if arr[idx] == -1:
        if idx == delete_node:
            continue
        else:
            visited_arr[idx] = True
            for e in node[idx]:
                if e != -2:
                    queue.append(e)
            if len(queue) == 0:
                leaf_count += 1
                continue
            while queue:
                x = queue.popleft()
                visited_arr[x] = True
                if len(node[x]) == 0:
                    leaf_count += 1
                else:
                    for child_node in node[x]:
                        if not visited_arr[child_node] and child_node != -2:
                            visited_arr[child_node] = True
                            queue.append(child_node)
print(leaf_count)
