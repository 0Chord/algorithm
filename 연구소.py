import copy

n, m = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

zero_count = 0
two_arr = []
max_arr = []
for col in range(n):
    for row in range(m):
        if arr[col][row] == 2:
            two_arr.append((col, row))


def dfs(graph, col, row):
    if col <= -1 or col >= n or row <= -1 or row >= m:
        return

    if graph[col][row] == 0:
        graph[col][row] = 2
        dfs(graph, col + 1, row)
        dfs(graph, col - 1, row)
        dfs(graph, col, row + 1)
        dfs(graph, col, row - 1)
    elif graph[col][row] == 1 and graph[col][row] == 2:
        return


for first_col in range(n):
    for first_row in range(m):
        if arr[first_col][first_row] == 0:
            for second_col in range(n):
                if first_col <= second_col:
                    for second_row in range(m):
                        if arr[second_col][second_row] == 0:
                            for third_col in range(n):
                                if first_col <= third_col:
                                    if second_col <= third_col:
                                        for third_row in range(m):
                                            if arr[third_col][third_row] == 0:
                                                if first_col != second_col or first_row != second_row:
                                                    if first_col != third_col or first_row != third_row:
                                                        if second_col != third_col or second_row != third_row:
                                                            copy_arr = copy.deepcopy(arr)
                                                            copy_arr[first_col][first_row] = 1
                                                            copy_arr[second_col][second_row] = 1
                                                            copy_arr[third_col][third_row] = 1
                                                            for lst in two_arr:
                                                                dfs(copy_arr, lst[0] + 1, lst[1])
                                                                dfs(copy_arr, lst[0] - 1, lst[1])
                                                                dfs(copy_arr, lst[0], lst[1] + 1)
                                                                dfs(copy_arr, lst[0], lst[1] - 1)
                                                            count = 0
                                                            for col in range(n):
                                                                for row in range(m):
                                                                    if copy_arr[col][row] == 0:
                                                                        count += 1
                                                            if zero_count < count:
                                                                max_arr = copy_arr
                                                            zero_count = max(zero_count, count)
print(zero_count)
