import sys
from collections import deque
from copy import deepcopy

n, m, r = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
r_list = list(map(int, sys.stdin.readline().rstrip().split()))
lst = []
n_num, m_num = n, m
queue = deque()
for el in r_list:
    if el == 1:
        lst = [[0] * m_num for _ in range(n_num)]
        for row in range(m_num):
            for col in range(n_num - 1, -1, -1):
                queue.append(arr[col][row])
        for row in range(m_num):
            for col in range(n_num):
                lst[col][row] = queue.popleft()
    elif el == 2:
        lst = [[0] * m_num for _ in range(n_num)]
        for col in range(n_num):
            lst[col] = arr[col][::-1]
    elif el == 3:
        tmp = n_num
        n_num = m_num
        m_num = tmp
        lst = [[0] * m_num for _ in range(n_num)]
        for row in range(n_num):
            for col in range(m_num - 1, -1, -1):
                queue.append(arr[col][row])

        for col in range(n_num):
            for row in range(m_num):
                lst[col][row] = queue.popleft()
    elif el == 4:
        tmp = n_num
        n_num = m_num
        m_num = tmp
        lst = [[0] * m_num for _ in range(n_num)]
        for row in range(n_num - 1, -1, -1):
            for col in range(m_num):
                queue.append(arr[col][row])
        for col in range(n_num):
            for row in range(m_num):
                lst[col][row] = queue.popleft()
    elif el == 5:
        lst = [[0] * m_num for _ in range(n_num)]
        for col in range(n_num // 2):
            for row in range(m_num // 2):
                queue.append(arr[col + n_num // 2][row])
            for row in range(m_num // 2):
                queue.append(arr[col][row])
        for col in range(n_num // 2):
            for row in range(m_num // 2, m_num):
                queue.append(arr[col + n_num // 2][row])
            for row in range(m_num // 2, m_num):
                queue.append(arr[col][row])
        for col in range(n_num):
            for row in range(m_num):
                lst[col][row] = queue.popleft()
    elif el == 6:
        lst = [[0] * m_num for _ in range(n_num)]

        for col in range(n_num // 2):
            for row in range(m_num // 2, m_num):
                queue.append(arr[col][row])
            for row in range(m_num // 2, m_num):
                queue.append(arr[col + n_num // 2][row])

        for col in range(n_num // 2):
            for row in range(m_num // 2):
                queue.append(arr[col][row])
            for row in range(m_num // 2):
                queue.append(arr[col + n_num // 2][row])
        for col in range(n_num):
            for row in range(m_num):
                lst[col][row] = queue.popleft()
    arr = deepcopy(lst)
for e in lst:
    print(*e)
