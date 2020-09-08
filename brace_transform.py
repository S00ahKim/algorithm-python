'''
프로그래머스
괄호 변환 (2020 카카오)

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

문제를 그대로 구현했다. v가 ""일 경우를 설정하지 않으면 재귀가 멈추지 않음.
'''
def solution(string):
    op = 0
    cl = 0
    if is_right(string):
        return string
    else:
        return transform(string)  

def transform(string):
    op = 0
    cl = 0
    u = ""
    v = ""
    answer = ""
    for idx in range(len(string)):
        if string[idx] == '(':
            op += 1
        else:
            cl += 1
        if op==cl:
            u = string[:idx+1]
            try:
                v = string[idx+1:]
            except:
                pass
            break
    if is_right(u):
        if v == "":
            return answer + u
        else:
            return answer + u + transform(v)
    else:
        if v == "":
            return answer + "(" + ")" + ff(u)
        else:
            return answer + "(" + transform(v) + ")" + ff(u)

def is_right(string):
    op = 0
    cl = 0
    for s in string:
        if s == '(':
            op += 1
        else:
            cl += 1
        if op < cl:
            return False
    return True

def ff(u):
    if len(u) > 2:
        u = u[1:-1]
        rp = str.maketrans('()', ')(')
        u = u.translate(rp)
        return u
    else:
        return ""

print(solution("(()())()") == "(()())()")
print(solution(")(")) # == "()"
print(solution("()))((()")) # == "()(())()"



# 추천을 많이 받은 다른 사람의 풀이
# ()를 파이썬에서 True로 인식하는 것을 활용함. 이렇게 간단할 수가...

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))