'''
백준 2613
https://www.acmicpc.net/problem/2613
'''

# 입력
n, m = map(int, input().split())
input_marbles = input().split(' ')

marbles=[] #전체 구슬 리스트
grouped=[] #그룹 안 구슬 갯수 리스트
for i in range(n):
    marbles.append(int(input_marbles[i]))

# 파라메트릭 서치
left = 1
right = n * 100

def is_possible(mid,m):
    count=0
    tmp_sum=0
    tmp_grouped=[0] * (m+1)
    for i in range(n):
        if marbles[i]>mid:
            return [False]
        if tmp_sum+marbles[i] > mid:
            tmp_sum=marbles[i]
            count += 1
        else:
            tmp_sum += marbles[i]
        if count>=m:
            return [False]
        tmp_grouped[count] += 1
    return [True, tmp_grouped]

while left<right:
    mid = (left+right)>>1
    #print(mid)
    isp = is_possible(mid,m)
    if isp[0] == True:
        grouped= isp[1]
        result=mid
        right=mid
    else:
        left=mid+1

# 0이 있는 그룹을 제외
for i in range(m):
    if grouped[i] == 0:
        idx = i-1
        grouped[i] += 1
        while True:
            if grouped[idx] == 1:
                idx -= 1
                continue
            break
        grouped[idx] -= 1

# 결과 출력
print(result)
grouped = grouped[:-1]
print(*grouped)