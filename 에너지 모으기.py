import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

max_energy = -1


def recur(lst, calc):
    global max_energy
    if len(lst) == 2:
        max_energy = max(calc, max_energy)
        return
    else:
        for idx in range(1, len(lst) - 1):
            clone_lst = lst[::]
            cal = calc + clone_lst[idx - 1] * clone_lst[idx + 1]
            clone_lst.pop(idx)
            recur(clone_lst, cal)


recur(arr, 0)
print(max_energy)
