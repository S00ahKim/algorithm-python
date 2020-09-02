'''
프로그래머스
기능 개발

1. 완료까지 걸리는 날짜를 구한다
2. 자기 자신보다 작거나 같은 날짜를 센다
3. 센 개수를 리턴한다.
'''
import math

def solution(progresses, speeds):
    answer = []
    length_of_arr = len(progresses)
    if length_of_arr == 1:
        return [1]
    left = [math.ceil((100-progresses[idx])/speeds[idx]) for idx in range(length_of_arr)]
    prev = left[0]
    answer.append(1)
    
    for l in left[1:]:
        if l <= prev:
            answer[-1] = answer[-1] + 1
        else:
            answer.append(1)
            prev = l
    return answer

print(solution([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))

# 추천을 많이 받은 다른 사람의 풀이
# ceil을 쓰지 않으려고 (p-100) => 음수, (p-100) // s => 내림한 음수(음수에서 내림은 절대값은 커짐), -((p-100)//s) => 올림한 양수
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]