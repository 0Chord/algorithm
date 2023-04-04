def solution(s):
    arr = list(s)
    answer = True
    queue = []
    for el in arr:
        if el == "(":
            queue.append("(")
        elif el == ")":
            try:
                queue.pop()
            except:
                return False
    if queue != []:
        return False
    return True