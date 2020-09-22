'''
프로그래머스
조이스틱

ord('A') = 65
ord('Z') = 90
'''

# 중간에 방향을 바꾸는 방법이 고려가 안 되어 있다.
def _solution(name):
    answer = 0
    forward = [n for n in range(65,91)]
    backward = [n for n in range(91,64,-1)]

    # 알파벳 조종
    for n in name:
        f = forward.index(ord(n))
        b = backward.index(ord(n))
        if f >= b:
            answer += b
        else:
            answer += f
    
    # 좌우 커서
    if name[1] == 'A':
        answer += len(name) - 2
    else:
        answer += len(name) - 1
    return answer


def solution(name):
    arr = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    answer = 0
    locat = 0
    while 1:
        answer += arr[locat]
        arr[locat] = 0
        if sum(arr) == 0: break
        left = 1
        right = 1
        while arr[locat + right] == 0:
            right += 1
        while arr[locat - left] == 0:
            left += 1
        if left >= right:
            locat += right
            answer += right
        else:
            locat -= left
            answer += left
    return answer


print(solution('JEROEN')) #56
print(solution('JAN')) #23