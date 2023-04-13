from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    order_queue = deque()
    for i in range(len(queue)):
        order_queue.append(i)
    cnt = 0
    while True:
        if order_queue[0] == location and queue[0] == max(queue):
            cnt += 1
            return cnt
        elif queue[0] == max(queue):
            queue.popleft()
            order_queue.popleft()
            cnt += 1
        else:
            q_pop = queue.popleft()
            o_pop = order_queue.popleft()
            queue.append(q_pop)
            order_queue.append(o_pop)
