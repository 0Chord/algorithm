from collections import deque


def solution(progresses, speeds):
    queue = deque(progresses)
    speed_queue = deque(speeds)
    res = []
    while queue:
        for i in range(len(queue)):
            queue[i] += speed_queue[i]
        cnt = 0
        while True:
            if len(queue) == 0:
                break
            if queue[0] < 100:
                break
            if queue[0] >= 100:
                cnt += 1
                queue.popleft()
                speed_queue.popleft()
        if cnt > 0:
            res.append(cnt)
    return res
