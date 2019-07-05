# 내 풀이 (1) : 효율성 실패, 정확성 성공

def solution(participant, completion):
    answer = ''
    for p in range(len(participant)):
        if participant[p] in completion:
            completion.remove(participant[p])
        else:
            answer = participant[p]
            
    return answer

# 내 풀이 (2) : 완주 못한 사람은 무조건 1명이고, 이름은 20자라는 조건을 활용

def solution(participant, completion):
    completion.append('z'*20)
    for (p, c) in zip(sorted(participant), sorted(completion)):
        if p != c: 
            return p

# 추천을 많이 받은 다른 사람의 풀이 : collections를 활용함
# collections: 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는 데에 사용하는 객체
#               참고: https://excelsior-cjh.tistory.com/94

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]