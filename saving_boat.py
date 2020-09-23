'''
프로그래머스
구명보트

- 최대 두 명만 탈 수 있음
- 최소 횟수로 구출
'''

# 정확성 테스트 통과, 효율성 시간 초과
def _solution(people, limit):
    answer = 0
    while people:
        a = people[0]
        try:
            b = max([p for p in people[1:] if p <= limit-a])
        except:
            b = ''
        if b == '':
            del people[0]
        else:
            del people[0]
            del people[people.index(b)]
        answer+=1
    return answer

# 두명만 탈 수 있기 때문에 최소값으로 넣어주기 위해서
# 가장 몸무게가 적은 사람과 비교하여 들어갈 수 있으면 두명이서 타고 
# 아니면 혼자 타도록 한다.
def solution(people, limit):
    answer = len(people)
    p = sorted(people,reverse = True)
    s,e = 0, len(p)-1
    while s < e : 
        if p[s]+p[e] <= limit :
            e-=1
            answer-=1
        s+=1
    return answer
    
print(solution([70, 50, 80, 50], 100)) #3
print(solution([70, 80, 50], 100)) #3