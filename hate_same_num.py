# 내 풀이
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) > 0:
            if i == answer[-1]:
                pass
            else:
                answer.append(i)

        else:
            answer.append(i)
    return answer

# 추천을 많이 받은 다른 사람의 풀이
# 슬라이싱을 할 때에는 리스트가 비었거나 범위 초과해도 오류나지 않는다.
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a