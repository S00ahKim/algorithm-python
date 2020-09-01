'''
프로그래머스
완주하지 못한 선수

1. 참가 배열 최대길이 10만
2. 낙오자는 1명
3. 동명이인 존재
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
    return participant[-1]

print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))

# 추천을 많이 받은 다른 사람의 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]