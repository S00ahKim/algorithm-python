'''
프로그래머스
체육복
'''
def solution(n, lost, reserve):
    lost_but_reserve = list(set(lost)&set(reserve))
    lost = sorted([l for l in lost if l not in lost_but_reserve])
    reserve = sorted([l for l in reserve if l not in lost_but_reserve])
    '''
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve] 라고 만든 코드가 있었는데, 
    난 굳이 교집합을 안 만들어도 되는데 만들었던 것 같다. 최대한 새 변수 생성을 안 하려고 해봐야겠다.
    '''
    answer = n - len(lost) # 이 부분을 맨 앞이 아니라 뒤에 써줘야 함.

    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
        else:
            pass
    return answer

print(solution(5, [2, 4], [1, 3, 5])) #5
print(solution(5, [2, 4], [3])) #4
print(solution(3, [3], [1])) #2