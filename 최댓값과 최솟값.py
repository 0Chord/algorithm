def solution(s):
    lst = list(map(int,s.split(" ")))
    max_num = max(lst)
    min_num = min(lst)
    answer = str(min_num) + " " + str(max_num)
    return answer