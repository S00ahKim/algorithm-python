'''
프로그래머스
더 맵게

풀이
1. 최소힙을 만든다
2. 배열 scoville을 최소힙에 insert한다
3. 음식 섞기 연산 후 다시 최소힙을 구성한다
4. 루트 노드가 K 이상이 될 때까지 1~3을 수행한다
5. 루트 노드밖에 남지 않았음에도 K이상이 되지 않았다면 -1을 리턴한다.

참고
힙(heap)은 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 자료구조이다.
'''
import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heapq.heappush(h, s) # 다른 사람 풀이에서는 hq.heapify(scoville)를 사용
    
    while True:
        _min = heapq.heappop(h)   
        if _min >= K:
            return answer
        if len(h) == 0:
            if _min < K:
                return -1
        _minsec = heapq.heappop(h)

        new = _min + (_minsec * 2)
        answer += 1
        heapq.heappush(h, new)

print(solution([1,2,3], 11))