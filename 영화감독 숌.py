import sys

n = int(sys.stdin.readline().rstrip())

cnt = 1

result = 666

while True:
    if cnt == n:
        print(result)
        break
    result += 1
    if "666" in str(result):
        cnt += 1
