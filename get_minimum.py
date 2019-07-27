# 재귀: 효율성 실패
def solution(A,B):
    return calculate(A, B, 0)

def calculate(a,b,n):
    minimum = min(a)
    maximum = max(b)
    a.remove(minimum)
    b.remove(maximum)
    n = n + minimum*maximum
    if len(a) == 0 :
        return n
    else: 
        return calculate(a, b, n)

# 일반 연산 구현
def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    result = 0
    for i in range (len(A)):
        result = result + A[i] * B[i]
    
    return result

# 간단하게 표현하기
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))