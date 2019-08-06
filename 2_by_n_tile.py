# 내 풀이 (효율성 실패)
def solution(n):
    d = [0,1,2]

    #i-1칸까지 채우고 하나 깔거나 i-2칸까지 채우고 가로로 깔고 두 개 까는 경우의 합
    for i in range(3,n+1): 
        d.append(d[i-1] + d[i-2])

    return d[n] % 1000000007

# 내 풀이 (통과)
# 파이썬 배열의 최대 크기가 536870912라서 실패한 것 같아 계속 변수 재할당하는 식으로 함

def solution(n):
    a = 0
    b = 1
    c = 2

    if n <= 3 : return n
    for i in range(3,n+1): 
        answer = b + c
        b = c
        c = answer

    return answer % 1000000007

# 추천을 많이 받은 다른 사람의 풀이
def tiling(n):
    a,b=1,1
    for i in range(n):a,b=b,a+b
    return a%100000 #개정 전 문제