def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(0,len(phone_book)) :
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return True
    return False