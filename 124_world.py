# 나의 풀이
# 나머지가 있는 경우는 솔루션(몫)+나머지, 없는 경우는 솔루션(몫-1)+4 로 나타나기 때문에 경우를 나눔

def solution(n):
    answer = ''
    if n%3 > 0:
        if n//3 > 0:
            front = ''+ solution(n//3)
            back = str(n%3)
            answer = front+back
        else:
            answer = str(n%3)
    else:
        if n//3 > 0:
            front = ''+ solution(n//3 -1)
            back = '4'
            answer = front+back
        elif n//3 == 0:
            answer = ''
        else:
            answer = str(n%3)

    return answer

# 추천을 많이 받은 다른 사람의 풀이
# 배열과 while 문을 활용. if를 안 쓰고 풀이하는 방법이 재미있었다.

def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

# 문자열의 인덱스를 활용.

def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]