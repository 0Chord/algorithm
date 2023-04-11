def solution(s):
    arr = s[1:-1]
    stack = []
    lst = []
    string = ""
    for el in arr:
        if el == "{":
            stack.append("{")
        elif el != "}" and len(stack) == 1:
            string += el
        elif el == "}":
            stack = []
            lst.append(string)
            string = ""
    for idx in range(len(lst)):
        lst[idx] = list(map(int, lst[idx].split(",")))
    lst.sort(key=lambda x: len(x))
    answer = []
    for idx in range(len(lst)):
        for el in lst[idx]:
            if el not in answer:
                answer.append(el)
    return answer
