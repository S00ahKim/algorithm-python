# 내 풀이
def solution(phone_book):
    if len(phone_book) == 1:
        return False
    phone_book.sort() #이부분을 하지 않으면 오류
    for i in range(len(phone_book)):
        for k in range(i+1, len(phone_book)):
            prefix = phone_book[i]
            word = phone_book[k]
            if word.find(prefix) == 0:
                print(word, prefix)
                return False
    return True

# 추천을 많이 받은 다른 사람의 풀이

# 깔끔
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# 해시 사용
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer