'''
프로그래머스
프린터

1. 가장 앞의 문서 꺼냄
2. 중요도 비교 -> 높은 게 있으면 마지막으로 보냄
                -> 아니면 인쇄
'''

def solution(priorities, location):
    is_mine = [0] * len(priorities)
    is_mine[location] = 1
    pairs = list(zip(priorities, is_mine))
    mine_out = False
    count_out = 0
    while not (mine_out):
        j = pairs[0]
        if j[0] == max(priorities):
            count_out += 1
            priorities.remove(j[0])
            if j[1] == 1:
                mine_out = True
            pairs = pairs[1:]
        else:
            pairs = pairs[1:] + [j]
    return count_out

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))

# 추천을 많이 받은 다른 사람의 풀이 - any를 사용하여 간단하게 풀었다.
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer