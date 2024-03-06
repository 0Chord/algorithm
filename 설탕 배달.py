import sys

n = int(sys.stdin.readline().rstrip())

result = -1
cnt = 5000
for five in range(1001):
    for three in range(1501):
        if five * 5 + three * 3 > 5000:
            break
        if n == five * 5 + three * 3:
            cnt = min(cnt, five + three)
            break

if cnt != 5000:
    result = cnt
print(result)
