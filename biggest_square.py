'''
백준 1915 가장 큰 정사각형

n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.
4 4
0100
0111
1110
0010

출력: 첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.
4
'''
from copy import deepcopy as dcp

n, m = map(int, input().split())
arr = []
dp = [[0]*(m) for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input())))

max_num = arr[0][0] #가장 작은 경우

for row_idx in range(1,n):
    for col_idx in range(1, m):
        if row_idx == 0:
            dp[row_idx][col_idx] = arr[row_idx][col_idx]
            if dp[row_idx][col_idx] > max_num:
                max_num = dp[row_idx][col_idx]
        else:
            if arr[row_idx][col_idx] == 1:
                dp[row_idx][col_idx] = min(dp[row_idx][col_idx-1], dp[row_idx-1][col_idx], dp[row_idx-1][col_idx-1]) + 1
                if dp[row_idx][col_idx] > max_num:
                    max_num = dp[row_idx][col_idx]

if max_num == 0:
    print(0)
else:                
    print(max_num*max_num)

#=======================================================================
n, m = map(int, input().split()) 
alist = list() 
for _ in range(n): 
    alist.append(list(map(int, input())))

dp_arr = dcp(alist)  
ans = dp_arr[0][0] # (1, 1)부터 탐색할 것이므로 범위에 없는 (0, 0)을 초기값으로 저장.

for i in range(1, n): 
    for j in range(1, m): 
        if alist[i][j]: # 정사각형의 맨 오른쪽 아래 모서리를 포함한 정사각형의 최대 크기를 저장
            # 해당 영역의 왼쪽 위쪽, 대각선 위쪽의 값중 
            # 가장 최솟값이 곧 1로만 이루어진 정사각형 크기의 최댓값이므로 해당 크기 +1을 더함
            dp_arr[i][j] = min(dp_arr[i-1][j], dp_arr[i][j-1], dp_arr[i-1][j-1]) + 1 
        ans = max(ans, dp_arr[i][j]) # 매번마다 가장 큰 크기를 저장.

print(ans * ans)  # 최댓값의 넓이를 출력