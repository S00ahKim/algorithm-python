'''
투빅스 (1주차 3번)

문제: 당신은 투빅스시의 텔레마케터이다. 
보유한 고객들의 전화번호를 통해 전화를 거는 것이 일인데 현재 보유한 전화번호부는 가짜번호가 너무 많다. 
또한 번호 안에 ‘-’(hyphen)이 존재해서 일처리가 번거롭다.
가짜번호를 구별하는 방법은 두가지이다. 
첫째로 투빅스시에서 개통된 전화번호는 중간의 4자리 수가 뒤의 4자리 수보다 크다. 
둘째로 앞의 3자리 수는 항상 010이어야 한다. 
기존의 전화번호부로부터 새로운 전화번호부를 만들어 일의 효율을 높여보자.

입력
‘phone_book.txt’는 ‘xxx-xxxx-xxxx’ 포맷의 전화번호(>=1)가 줄로 구분 되어있다.

출력
‘new_phone_book.txt‘는 ‘010aaaabbbb’ 포멧(aaaa>bbbb)의 전화번호(>=0)가 줄로 구분 되어있다.
'''

phone_book = open('phone_book.txt', 'r')
new_phone_book = open('new_phone_book.txt', 'w')

lines = phone_book.readlines()
for line in lines:
    pn = line.split('-')
    if pn[0] == '010':
        if pn[1] > pn[2]:
            new_phone_book.write(''.join(pn))
    else:
        pass

phone_book.close()
new_phone_book.close()