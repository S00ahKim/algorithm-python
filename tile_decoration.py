# 내 풀이
def solution(N):
    length = [1, 1]
    for i in range(2, 80):
        tmp = length[i-2] + length[i-1]
        length.append(tmp)

    answer = [4]
    for i in range(1,80):
        tmp = answer[i-1] + length[i]*2
        answer.append(tmp)

    return answer[N-1]

# 추천을 많이 받은 다른 사람의 풀이
# 내 풀이와 유사하지만 좀 더 메모리 활용을 잘하고 쓸데없는 변수 사용이 없다.
def solution(N):
    l=[1,1]
    for i in range(2,N):
        l.append(l[-1]+l[-2])
    answer = (l[-1]*2+l[-2])*2
    return answer