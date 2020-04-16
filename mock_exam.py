'''
프로그래머스
모의고사

1. 1번 수포자: 순서대로 1~5 / 12345
2. 2번 수포자: 홀수는 2, 짝수는 1,3,4,5 / 21232425 
3. 3번 수포자: 3,1,2,4,5 각 2번씩 / 3311224455
'''
def solution(answers):   
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            cnt[0] += 1
        
        if answers[i] == stu2[i%8]:
            cnt[1] += 1
        
        if answers[i] == stu3[i%10]:
            cnt[2] += 1

    maximum = max(cnt)
    if cnt[0] == maximum:
        answer.append(1)  
    if cnt[1] == maximum:
        answer.append(2)
    if cnt[2] == maximum:
        answer.append(3)  
    return answer

print(solution([1,2,3,4,5]))

# 다른 사람의 풀이
# 패턴을 제너레이터로 처리하여 공간복잡도를 고려함

from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
