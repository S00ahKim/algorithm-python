# 내 풀이 : 너무 꼬아 생각해서 틀렸음. 간단하게 접근.
def solution(prices):
    answer = []
    for i in range(len(prices)):
        for p in range(i+1, len(prices)):
            if prices[i] > prices[p]:
                break
        answer.append(p-i)
    return answer

# 추천을 많이 받은 다른 사람의 풀이

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer