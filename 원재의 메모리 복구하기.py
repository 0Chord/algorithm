T = int(input().rstrip())

for t in range(1, T + 1):
    memory_arr = list(input().rstrip())
    count = 0
    for idx in range(len(memory_arr)):
        if memory_arr[idx] == '1':
            count += 1
            for mini_idx in range(idx, len(memory_arr)):
                if memory_arr[mini_idx] == '1':
                    memory_arr[mini_idx] = '0'
                elif memory_arr[mini_idx] == '0':
                    memory_arr[mini_idx] = '1'
    print("#"+str(t),count)
