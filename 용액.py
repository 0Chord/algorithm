import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
start = 0
end = n - 1
two_sum = int(1e10)
two_pointer = [0, 0]
while start < end:
    if arr[start] + arr[end] == 0:
        two_pointer[0] = start
        two_pointer[1] = end
        break
    else:
        if arr[start] + arr[end] < 0:
            if abs(arr[start] + arr[end]) < abs(two_sum):
                two_sum = abs(arr[start] + arr[end])
                two_pointer[0] = start
                two_pointer[1] = end
            start += 1
        else:
            if arr[start] + arr[end] < abs(two_sum):
                two_sum = abs(arr[start] + arr[end])
                two_pointer[0] = start
                two_pointer[1] = end
            end -= 1
print(arr[two_pointer[0]], arr[two_pointer[1]])
