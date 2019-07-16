# 내 풀이
def solution(n, lost, reserve):
    U = list(range(1, n+1))       #체육수업을 들을 수 있는 학생
    L = list(set(lost) - set(reserve))  #체육복을 잃어버린 학생
    R = list(set(reserve) - set(lost))  #여벌의 체육복
    for a in L:
        if (a + 1) not in R and (a - 1) not in R:   
            U.remove(a)
        elif (a + 1) in R and (a - 1) not in R:     
            R.remove(a + 1)
    return len(U)


# 추천을 많이 받은 다른 사람의 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
