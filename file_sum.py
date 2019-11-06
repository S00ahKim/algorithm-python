'''
백준 11066 파일 합치기
'''
import sys 

T = int(sys.stdin.readline()) 
K = [] 
file = [] 

for t in range(T): 
    K.append(int(sys.stdin.readline())) 
    file.append(list(map(int, sys.stdin.readline().split()))) 
    
for t in range(T): 
    k = K[t] 
    f = file[t] 
    sum = [f[0]]
    
    for i in f[1:]: 
        sum.append(i + sum[-1]) 
    accumulated = [[0] * k for _ in range(k)] 
    
    accumulated[0][1] = sum[1] 
    for i in range(1, k - 1): 
        accumulated[i][i + 1] = sum[i + 1] - sum[i - 1] 
    
    for gap in range(2, k): 
        for i in range(k - gap): 
            accumulated[i][i + gap] = float('inf') 
            
            for j in range(i, i + gap): 
                accumulated[i][i + gap] = min(accumulated[i][i + gap], accumulated[i][j] + accumulated[j + 1][i + gap]) 
                
            accumulated[i][i + gap] = accumulated[i][i + gap] + sum[i + gap] - sum[i - 1]
            if i > 0 else accumulated[0][gap] + sum[gap] 
                                            
    print(accumulated[0][k - 1])
