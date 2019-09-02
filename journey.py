'''
투빅스 (7주차 1번)
이영전은 여행을 떠나기 위해 최대 X kg 의 짐을 넣을 수 있는 배낭을 샀다. 
이영전에게는 N 개의 짐이 있는데, 배낭에 최대한 많은 무게의 짐을 넣을 것이다. 
이 때 배낭에 들어간 짐의 무게의 총 합을 구하라.

입력
1 이상 10 이하 자연수 N 과 1 이상 100 이하 자연수 X 가 한 줄에 공백을 구분하여 주어진다. 
다음 줄에는 자연수인 각 짐의 무게가 공백을 구분하여 주어진다.

출력
정답을 출력하라.
'''
from itertools import combinations

N, X  = (int(x) for x in input().split())
raw_burden = [int(x) for x in input().split()]
answer = 0
burden = []
for i in range(N):
    if raw_burden[i] < X:
        burden.append(raw_burden[i])
    elif raw_burden[i] == X:
        answer = raw_burden[i]

comb = []
if answer == 0:
    for n in range(1, N+1):
        tmp = list(combinations(burden, n))
        for t in tmp:
            if sum(t) <= X:
                comb.append(sum(t))
    answer = max(comb)

print(answer)