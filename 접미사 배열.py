arr = list(input().rstrip())
lst = []
for i in range(len(arr)):
    lst.append("".join(arr[i:]))
lst.sort()
for el in lst:
    print(el)
