import heapq

# 모듈을 사용하지 않으면 효율성 테스트에서 계속 실패하여 모범 답안만 옮김
# heapq 모듈: 이진 트리 기반의 최소힙 자료구조 제공. 항상 "정렬"된 상태로 추가/삭제되며 "최소값"은 항상 루트에 위치
# 위와 같은 heap의 특성 때문에 이 문제에서 힙을 쓰는 것
# 참고: https://www.daleseo.com/python-heapq/

def mixDishes(array, k):
    answer = 0 
    while 1:
        try:
             newDishValue = heapq.heappop(array) + heapq.heappop(array)*2
             heapq.heappush(array, newDishValue)
             answer += 1
             if array[0] >= k:
                 return answer
        except:
             return -1

def solution(array, k):

    heapq.heapify(array)
    answer = mixDishes(array, k)

    return answer
