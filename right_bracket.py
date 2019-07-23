# 내 풀이
def solution(s):
    string = list(s)
    stack = []
    
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    
    if len(stack) > 0:
        return False
    else:
        return True

# 다른 사람의 풀이
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0