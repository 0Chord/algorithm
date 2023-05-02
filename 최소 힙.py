import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = []

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, x)
