# 내 풀이
# 의상 종류별로 입지 않는 경우(1)를 추가하고, 모두 입지 않는 경우를 뺀다

def solution(clothes):
    dic = {}
    answer = 1
    for i in range(len(clothes)):
        key = clothes[i][1]
        tmp = []
        dic[key] = tmp
    for i in range(len(clothes)):
        category = clothes[i][1]
        dic[category].append(clothes[i][0])
    arr = list(dic.items())
    for i in range(len(arr)):
        a = len(arr[i][1])
        answer *= (a+1)
    answer -=1
    return answer

# 추천을 많이 받은 다른 사람의 풀이
# 아이디어는 같은데, 모듈을 이용하여 간편하게 풀이했다.

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer