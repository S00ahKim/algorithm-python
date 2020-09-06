'''
프로그래머스
이중 우선 순위 큐
'''
import heapq

def _solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        op = op.split(' ')
        if op[0] == "I":
            heapq.heappush(min_heap, int(op[1]))
            heapq.heappush(max_heap, (-1*int(op[1]), int(op[1])))
        else:
            if op[1] == "-1":
                # 최소값 삭제
                j = heapq.heappop(min_heap)
                max_heap.remove((-j, j))
            else:
                # 최대값 삭제     
                j = heapq.heappop(max_heap)[1]
                min_heap.remove(j)
    if len(min_heap) > 0:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0,0]

# 굳이 힙을 써야 하나 싶어서 다시
def solution(operations):
    answer=[]
    for i in operations:
        a,b=i.split(" ")
        if a=="I":
            answer.append(int(b))
        else:
            if len(answer)>0:
                if b=="1":
                    answer.pop()
                else:
                    answer.pop(0)
            else:
                pass
        answer.sort()
    if len(answer)==0:
        return [0,0]
    else:
        return [max(answer),min(answer)]

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

# 힙을 쓰고 싶을 때는 이렇게 하는 듯 하다.
# 추천을 많이 받은 다른 사람의 풀이
def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

# 2
def solution(operations):
    h=[]
    for i in operations:
        a,b=i.split(" ")
        if a=="I":
            heapq.heappush(h,int(b))
        else:
            if len(h)>0:
                if b=="1":
                    h.pop(h.index(heapq.nlargest(1,h)[0]))
                else:
                    heapq.heappop(h)
            else:
                pass
    if len(h)==0:
        return [0,0]
    else:
        return [heapq.nlargest(1,h)[0],heapq.nsmallest(1,h)[0]]