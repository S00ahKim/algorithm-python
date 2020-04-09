'''
프로그래머스
타겟 넘버

깊이 우선 탐색
=> 음수/양수의 두 가지 방법으로 수를 만들 수 있음
=> 모든 수를 다 써야 함
'''
def solution(numbers, target):
    sup= [0]
    for i in numbers: #주어진 숫자들에 대해서
        sub = []
        for j in sup : #이전 숫자로 만들 수 있는 숫자들에 대해
            sub.append(j+i) #양수 연산도
            sub.append(j-i) #음수 연산도 수행해본다
        sup = sub # 이번 숫자에서 진행한 결과를 이전 숫자들로 만들 수 있는 숫자들 리스트로 업데이트한다.
    return sup.count(target) # 계산했던 모든 경우에 대해 target이 나오는 횟수를 계산한다.


# 추천을 많이 받은 다른 사람의 풀이

def solution_(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
아이디어 자체는 비슷하다. 
재귀는 일을 추상적으로 확실히 분리한 후에 쓸 수 있는 알고리즘이라는 생각이 든다.

맨 앞의 수를 빼면 타깃이 만들 수 있는 수에서 그만큼 빠지거나(맨 앞의 수를 양수계산한 경우)
그만큼 더해져야 한다(맨 앞의 수를 음수계산한 경우)
그렇게 전체 리스트를 구하기 위해 작은 리스트에 대해 연산, 더 작은 리스트에 대해 연산하며 재귀를 수행.
'''