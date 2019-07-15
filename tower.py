# 내 풀이
# 이 문제의 풀이는 추천을 많이 받은 사람의 풀이와 내 풀이가 일치했다

def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)-1, 0, -1):
        for k in range(i-1, -1, -1):
            if heights[k] > heights[i]:
                answer[i]= k+1
                break
    return answer
