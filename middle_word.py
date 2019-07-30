# 내 풀이

def solution(s):
    word = list(s)
    if len(word) == 1:
        return s
    elif len(word)%2 >0:
        return word[int((len(word)-1)/2)]
    else:
        return word[int(len(word)/2-1)]+word[int(len(word)/2)]
    return answer

# 추천을 많이 받은 다른 사람의 풀이

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]