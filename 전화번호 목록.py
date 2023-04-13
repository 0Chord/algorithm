def solution(phone_book):
    if len(phone_book) == 1:
        return False
    else:
        phone_book.sort()
        for i in range(len(phone_book) - 1):
            if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
                return False
            else:
                continue
        answer = True
        return answer
