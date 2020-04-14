'''
프로그래머스
전화번호 목록
'''
def solution(phone_book): 
    phone_book.sort(key=lambda s:len(s)) 
    for pp in phone_book: 
        for p in phone_book: 
            if pp in p and p != pp and pp[0]==p[0]: 
                return False 
    return True

# 추천을 많이 받은 다른 사람의 풀이
def solution(phoneBook): 
    phoneBook = sorted(phoneBook) 
    for p1, p2 in zip(phoneBook, phoneBook[1:]): 
        if p2.startswith(p1): 
            return False 
    return True