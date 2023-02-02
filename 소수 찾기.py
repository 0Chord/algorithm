import itertools

count = 0


def solution(numbers):
    global count
    answer = 0
    number_list = list(numbers)
    visited_set = []
    for idx in range(len(numbers)):
        for el in (list(itertools.permutations(number_list, idx + 1))):
            num = int("".join(list(el)))
            if not num in visited_set:
                visited_set.append(num)
                if prime(num):
                    count += 1
    return count


def prime(number):
    if number < 2:
        return False
    check = True
    for j in range(2, int(number ** 0.5) + 1):
        if number % j == 0:
            check = False
            break
    if check:
        return True
    return False
