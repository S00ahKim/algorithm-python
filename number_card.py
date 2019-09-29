'''
백준 10815
숫자 카드

처음에는 set()으로 해서 교집합을 구했으나 시간 초과 발생.
dict 타입은 해시테이블 알고리즘을 사용하여 시간 단축.
'''
import sys
input = sys.stdin.readline

N=int(input())
have = input().split()

M=int(input())
check = input().split()

dic = dict()
for h in have:
    dic[h] = 1

ans = ""
for m in range(M):
    try:
        ans += str(dic[check[m]])
    except:
        ans += '0'
    finally: #에러가 나더라도 실행
        ans += ' '

print(ans[:len(ans)-1])