'''
프로그래머스
소수 찾기
'''
from itertools import permutations

def solution(numbers):
    answer = 0
    n = list(numbers)
    n.sort(key=int, reverse=True)
    length = int(''.join(n)) + 1

    # 에라토스테네스의 체 (소수 아닌 것 1)
    is_pn = [0]*length
    is_pn[0] = 1
    is_pn[1] = 1
    for i in range(2, length):
        t = i+i
        while t < length:
            is_pn[t] = 1
            t += i

    # 주어진 수로 만들 수 있는 수 구하기
    new_s = list(n)
    for i in range(2,len(n)+1):
        pm = list(permutations(n, i))
        for j in pm:
            if len(j) <= len(n):
                new_s.append(''.join(j))
    new_s = list(set([int(x) for x in new_s]))
    
    # 구하기
    for s in new_s:
        if is_pn[s] == 0:
            answer += 1
    return answer

print(solution('011'))


# 추천을 많이 받은 다른 사람의 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
