'''
프로그래머스
디스크 컨트롤러

1. 작업 중일 때 들어온 것들 -> 대기시간+수행시간 해서 작은 것부터 처리
2. 작업 중이지 않을 때 -> 먼저 들어온 것부터 처리

0 1 2 3
  9(+2)     2+9+(1+6+9)+(3+1+9) = 3x+y+z = 33+7+4
    6(+1)   1+6+(2+9+6)+(3+1+6) = 3y+x+z = 21+11+4
    3(+1)   1+3+(1+6+3)+(2+9+3) = 3z+x+y = 12+11+7 
굳이 다 계산 안 해도 대기시간+수행시간이 최소면 됨.
'''
import heapq

# 런타임 에러
def solution(jobs):
    len_of_jobs = len(jobs)
    doing = False
    now = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    
    while jobs:
        if not doing:
            j = jobs.pop(0)
            now += j[0] + j[1] 
            doing = True
        else:
            candidate = [j for j in jobs if j[0] <= now]
            if len(candidate) == 0:
                doing = False
            else:
                min_heap = []
                for c in candidate:
                    heapq.heappush(min_heap, (now - c[0] + c[1], c))
                j = heapq.heappop(min_heap)[1]
                jobs.remove(j)
                now = now + now - j[0] + j[1]
    return now/len_of_jobs

print(solution([[0, 3], [1, 9], [2, 6]]))

# 다른 사람의 풀이
# 아이디어는 유사한데 매번 힙을 생성하는 게 아니라 미리 만들어둔다는 것이 다르다.
def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer//len(jobs)