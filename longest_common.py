'''
3. 최장 공통 부분 순서의 길이와 함께 최장 공통 부분 순서도 같이 구할 수 있도록 작성하시오.
'''
def lcs(x,y):
    x = '_'+x
    y = '@'+y
    m = len(x)
    n = len(y)
    C = [[0]*(n) for i in range(m)]
    B = [[0]*(n) for i in range(m)]
    ans = []

    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                C[i][j] = C[i-1][j-1]+1
                B[i][j] = 'D'
            else:
                if C[i-1][j] >= C[i][j-1]:
                    C[i][j] = C[i-1][j]
                    B[i][j] = 'U'
                else:
                    C[i][j] = C[i][j-1]
                    B[i][j] = 'L'

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
        else:
            break
    answer = ''.join(reversed(ans))

    return (C[m-1][n-1], answer)

print('LCS 길이', lcs('ACAYKP','CAPCAK')[0])
print('LCS 문자열', lcs('ACAYKP','CAPCAK')[1])
