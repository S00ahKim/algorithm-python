'''
프로그래머스
h 인덱스

h 이상 인용된 h개 이상의 논문
나머지는 h 이하 인용
'''

def solution(citations):
    citations.sort() #일단 정렬을 하는 아이디어까지는 똑같다.
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            # 이 부분이 엄청 간결하게 구현되어 있다. 
            return l-i
    return 0