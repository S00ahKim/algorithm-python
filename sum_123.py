'''
백준 9095: 1,2,3 더하기
'''
def sum_123(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return sum_123(n-1) + sum_123(n-2) + sum_123(n-3)
    
test = int(input())

for num in range(test):
    answer = sum_123(int(input()))
    print(answer)
