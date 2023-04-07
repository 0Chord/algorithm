from collections import deque


def solution(s):
    queue = deque(s)
    cnt = 0
    for i in range(len(s)):
        q = deque()
        flag = True
        if i != 0:
            x = queue.popleft()
            queue.append(x)
        for j in range(len(s)):
            if queue[j] == "[":
                q.append("[")
            elif queue[j] == "(":
                q.append("(")
            elif queue[j] == "{":
                q.append("{")
            elif len(q)>0:
                if queue[j] == "]" and q[-1] == "[":
                    q.pop()
                elif queue[j] == "]" and q[-1] != "[":
                    flag = False
                    break
                elif queue[j] == ")" and q[-1] == "(":
                    q.pop()
                elif queue[j] == ")" and q[-1] != "(":
                    flag = False
                    break
                elif queue[j] == "}" and q[-1] == "{":
                    q.pop()
                elif queue[j] == "}" and q[-1] != "{":
                    flag = False
                    break
            elif len(q) == 0:
                flag = False
                break
        if flag and len(q) == 0:
            cnt += 1
    return cnt
