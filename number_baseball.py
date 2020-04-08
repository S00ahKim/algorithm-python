'''
프로그래머스
숫자 야구

조건
1. 서로 다른 3자리 수
2. 0이 포함되지 않음 (1~9)

위 조건에 따라 가능한 숫자의 범위는 123~987
'''

def solution(baseball):
    candidates = [ str(i) for i in range(123, 988)]
    removed = set()

    for candidate in candidates:
        if candidate[0] == candidate[1] or candidate[0] == candidate[2] or candidate[1] == candidate[2]:
            removed.add(candidate)
            continue
        if '0' in candidate:
            removed.add(candidate)
            continue
        for result in baseball:
            if game(str(result[0]), candidate) == (result[1], result[2]):
                pass
            else:
                removed.add(candidate)

    return len(list(set(candidates)-set(removed)))

def game(given, byme):
    strike = 0
    ball = 0

    if given[0] == byme[0]:
        strike+=1
    else:
        if given[0] in byme:
            ball += 1
    if given[1] == byme[1]:
        strike+=1
    else:
        if given[1] in byme:
            ball += 1
    if given[2] == byme[2]:
        strike+=1
    else:
        if given[2] in byme:
            ball += 1

    return (strike, ball)

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))