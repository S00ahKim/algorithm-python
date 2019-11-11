'''
3. 최장 공통 부분 순서의 길이와 함께 최장 공통 부분 순서도 같이 구할 수 있도록 작성하시오.
'''
def lcs(x,y):
    x = '_'+x #첫줄 0을 만들기 위함
    y = '@'+y
    m = len(x)
    n = len(y)
    C = [[0]*(n) for i in range(m)]
    '''
    주의: 이차원 배열 초기화하는 방법
    # (X)
    list1 = [[0]*3]*3
    list1[0][0] = 1
    print list1 # [[1,0,0],[1,0,0],[1,0,0]]
    
    # (O)
    list2 = [[0]*3 for i in range(3)]
    list2[0][0] = 1
    print list2 # [[1,0,0],[0,0,0],[0,0,0]]
    '''
    B = [[0]*(n) for i in range(m)]
    ans = []

    # 최장 공통 부분 순서의 길이
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                C[i][j] = C[i-1][j-1]+1
                B[i][j] = 'D' #대각선
            else:
                if C[i-1][j] >= C[i][j-1]:
                    C[i][j] = C[i-1][j]
                    B[i][j] = 'U' #위로
                else:
                    C[i][j] = C[i][j-1]
                    B[i][j] = 'L' #왼쪽으로

    # 최장 공통 부분 순서
    point_r = m-1
    point_c = n-1
    while True:
        point = B[point_r][point_c]
        if point == 'U':
            point_r -= 1
        elif point == 'D':
            ans.append(x[point_r])
            point_r -= 1
            point_c -= 1
        elif point == 'L':
            point_c -= 1
        else: # == 0
            break
    answer = ''.join(reversed(ans)) #.reverse는 return하지 않아서 join이 안 됨

    return (C[m-1][n-1], answer)

print('LCS 길이', lcs('ACAYKP','CAPCAK')[0]) #4
print('LCS 문자열', lcs('ACAYKP','CAPCAK')[1]) #ACAK
