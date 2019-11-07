'''
백준 1890 점프
→와 ↓만 가능함. 
A와 B라는 칸에서 C로 갈 수 있다. 
칸C까지 갈 수 있는 경우의 수는 칸A와 칸B까지 갈 수 있는 경우의 수의 합.
'''
import sys # 인풋 시간 빠르게 하기 위함

N = int(sys.stdin.readline())
board = [] 

for i in range(N): # 보드 구성
    temp = list(map(int, sys.stdin.readline().split())) 
    board.append(temp)

dp = [] # dp 초기화
for i in range(N): 
    dp.append([])
    for j in range(N):
        dp[i].append(0)
 
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1: #마지막 칸에 가면 멈춤
            break
        value = board[i][j]
        down = i + value #아래로 가는 것
        right = j + value #옆으로 가는 것
 
        if down < N:
            dp[down][j] += dp[i][j]
        if right < N:
            dp[i][right] += dp[i][j]
 
print(dp[N-1][N-1])