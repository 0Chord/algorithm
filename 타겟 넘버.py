count = 0


def solution(numbers, target):
    answer = 0
    dfs(0, numbers, target, 0)
    return count


def dfs(idx, numbers, target, calc):
    global count
    if idx >= len(numbers):
        if calc == target:
            count += 1
        return
    minus_calc = calc - numbers[idx]
    plus_calc = calc + numbers[idx]

    dfs(idx + 1, numbers, target, minus_calc)
    dfs(idx + 1, numbers, target, plus_calc)
