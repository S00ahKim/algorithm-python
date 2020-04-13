'''
프로그래머스
위장

매일 다른 조합의 옷을 입어야 함
- 최소 하나는 필수
- 같은 종류는 한 번만 선택 가능
- 의상 이름은 모두 다름

의상 정보 2차원 배열에 대해 서로 다른 옷 조합 수 리턴

1. 의상 종류별로 의상 이름 리스트 만들기
2. 경우의 수 구하기
'''

def solution(clothes):
    answer = 1
    closet = dict()

    for c in clothes:
        if c[1] not in closet.keys():
            closet[c[1]] = []
        closet[c[1]].append(c[0])
    
    for key in closet.keys():
        answer *= len(closet[key]) + 1
    
    return answer-1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]) == 5)


# 다른 사람의 풀이
from collections import Counter #컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
from functools import reduce #입력 받은 컨테이너 타입(iterable)을 지정한 함수에 따라 계산한 후, 단일 값으로 결과를 반환

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


# 다른 사람의 풀이2
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1