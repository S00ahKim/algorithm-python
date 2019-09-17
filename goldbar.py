'''
투빅스 (9주차)

모험가 태한이는 금괴가 가득 있다는 신비로운 별장에 도착했다.
이 별장에는 N개의 방이 일렬로 배치되어 있고, 
각방의 문앞에는 금괴의 개수가 적혀있다. 
태한이는 다음과 같은 2가지 규칙을 따르며 각방의 금괴를 획득할 수 있다.

1.방을 선택하면, 그 방에 있는 금괴를 모두 가지고 와야한다.
2.연속된 3개의 방에 모두 들어갈 수는 없다.

태한이를 도와 금괴를 가장 많이 가져갈 수 있도록 하는 프로그램을 작성하세요.
예를들어, 6개의 방이 있고, 
각 방에 순서대로 6, 10, 13, 9, 8, 1개의 금괴가 들어 있을 때, 
1번째, 2번째, 4번째, 5번째 방을 선택하면 총 금괴의 개수가 33으로 최대가 된다.

'''
import itertools

N = int(input())
gold = []

for i in range(N):
	tmp = int(input())
	gold.append(tmp)
    
maximum = 0

if N <= 2:
    maximum = sum(gold)
else:
    for k in range(3, N):
        selected = itertools.combinations([i for i in range(N)], k)

        for case in selected:
            i = 2
            is_satisfied = True

            while i<k:
                if case[i-1] == case[i]-1 and case[i-2] == case[i]-2:
                    is_satisfied = False
                    break
                i += 1
            if is_satisfied:
                tmp = 0
                for idx in case:
                    tmp += gold[idx]
                if tmp > maximum:
                    maximum = tmp

print(maximum)