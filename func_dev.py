# 내 풀이

def solution(progresses, speeds):
    need = []
    answer = []

    for i in range(len(progresses)):
        x = (100 - progresses[i])//speeds[i]
        if ((100 - progresses[i])%speeds[i] != 0):
            x += 1
        need.append(x)
            
    idx = 0
    for i in range(len(need)):
        if need[idx] < need[i]: #이 반대의 경우를 else로 빼고 계산하면 변수가 꼬여서 안 풀림
            answer.append(i-idx)
            idx = i
    answer.append(len(need)-idx)

    return answer

# 추천을 많이 받은 다른 사람의 풀이

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds): #zip은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 함
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]