import sys

sys.setrecursionlimit(10000000)
k = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip().split())

min_num = 10000000000
max_num = -1

min_str = ""
max_str = ""


def recur(idx, numbers):
    global min_num, max_num, min_str, max_str
    if len(numbers) == k + 1:
        if min_num > int(numbers):
            min_num = int(numbers)
            min_str = numbers
        if max_num < int(numbers):
            max_str = numbers
            max_num = max(max_num, int(numbers))
        return
    flag = False
    for i in range(10):
        if arr[idx] == ">" and int(numbers[-1]) > i and str(i) not in numbers:
            recur(idx + 1, numbers + str(i))
            flag = True
        elif arr[idx] == "<" and int(numbers[-1]) < i and str(i) not in numbers:
            recur(idx + 1, numbers + str(i))
            flag = True
    if not flag:
        return


for num in range(10):
    recur(0, str(num))
print(max_str)
print(min_str)
