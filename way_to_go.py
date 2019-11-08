'''
1. 행렬 경로의 이동상의 규칙을 다음과 같이 적용한다 하자.  

- 오른쪽이나 아래쪽, 또는 오른쪽 대각선으로만 이동할 수 있다. (=> 오른쪽 하단만 해당한다고 여김)
- 왼쪽, 위쪽으로의 이동과 여타의 대각선 이동은 허용하지 않는다.

n x n 행렬의 왼쪽 위(1,1) 에서 시작해 오른쪽 아래(n,n)까지 한 칸씩 이동하여 도달할 때 
모든 경로의 점수 중 가장 높은 점수를 찾는 동적 프로그래밍 알고리즘을 작성하시오.

------------------------------------------------------------------------------------
행렬과 같은 크기의 DP 배열의 각 칸 안에 
해당 칸까지 규칙을 따라 갔을 때 얻을 수 있는 최고점을 저장한다. (메모이제이션)
해당 칸보다 더 도착지에 가까워지도록 문제를 확장할 때에는 거기에서 불러와서 쓴다.
문제가 정사각형 형태이기 때문에 1*1 => 2*2로 확장할 수 있어서 왼쪽, 위, 왼쪽대각선을 보면 됨.
'''
import sys

N = int(sys.stdin.readline()) #행렬 사이즈

board = [] 

for i in range(N): # 보드 구성
    temp = list(map(int, sys.stdin.readline().split())) 
    board.append(temp)

dp = [] # dp 초기화
for i in range(N): 
    dp.append([])
    for j in range(N):
        dp[i].append(0)

for i in range(N): # i는 행
    for j in range(N): #j는 열
        val = board[i][j]
        left = 0
        up = 0
        cross = 0
        if i-1 >= 0:
            up = dp[i-1][j]
        if j-1 >= 0:
            left = dp[i][j-1]
        if i-1 >= 0 and j-1 >= 0:
            cross = dp[i-1][j-1]

        dp[i][j] = val+max(up, left, cross)

print(dp[N-1][N-1])