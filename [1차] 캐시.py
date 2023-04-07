from collections import deque

def solution(cacheSize, cities):
    queue = deque()
    cache = 0
    times = 0
    if cacheSize == 0:
            return len(cities)*5
    for el in cities:
        if cache < cacheSize:
            if len(queue)==0:
                times += 5
                queue.append(el.lower())
                cache += 1
            elif el.lower() in queue:
                times += 1
                queue.remove(el.lower())
                queue.append(el.lower())
            else:
                queue.append(el.lower())
                times += 5
                cache += 1
        else:
            if el.lower() in queue:
                times += 1
                queue.remove(el.lower())
                queue.append(el.lower())
            else:
                queue.popleft()
                queue.append(el.lower())
                times += 5
    return times