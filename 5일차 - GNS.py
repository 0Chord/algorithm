number_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input().rstrip())

for t in range(1, T + 1):
    tc, tc_count = input().split()
    tc_count = int(tc_count)
    arr = input().split()
    middle_arr = []
    for el in arr:
        middle_arr.append(number_arr.index(el))
    middle_arr.sort()
    result_arr = []
    for el in middle_arr:
        result_arr.append(number_arr[el])
    print(tc)
    print(*result_arr)
