# 내 풀이

from sympy import Symbol, solve

def solution(brown, red):
    y=Symbol('y')
    equation = 2*y**2 - (brown+4)*y +2*(brown+red)
    answer = solve(equation)
    answer.sort()
    answer.reverse()
    return answer

def solution(b, r):
    for y in range(1, r+1):
        for x in range(y, r+1):
            if x * y == r and ((x + y) << 1) + 4 == b:
                return [x+2, y+2]
            elif x * y > r:
                break

# 추천을 많이 받은 다른 사람의 풀이

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]