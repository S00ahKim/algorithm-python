'''
투빅스 (5주차 4번)

문제
기윤이는 CxC크기(이때 C는 3^k꼴)의 텃밭이 있다. 이 텃밭의 각 칸에는 상추, 오이, 토마토 중 하나가 심어져 있다. 
이 텃밭을 적절한 크기로 나누려고 하는데, 이 때 다음 규칙에 따라 구역을 나누려고 한다.

1. 만약 같은 작물이 심어져 있다면 더 이상 구역을 나누지 않는다.
2. 1번을 만족하지 않는 경우, 텃밭을 같은 크기의 9개의 구역으로 나누고, 각 구역에 대해 1번의 과정을 반복한다.

위와 같이 구역을 나누었을 때, 상추만 심어진 구역의 개수, 오이만 심어진 구역의 개수, 토마토만 심어진 구역의 개수를 구하는 프로그램을 작성하라.

입력
첫째 줄에 C(1<=C<=3^7, C는 3^k꼴이다)가 주어진다. 다음 C개의 줄에는 C개
의 정수로 행렬이 주어진다. 단 상추는 -1, 오이는 0, 토마토는 1로 표현한다. 

출력
첫째 줄에 상추만 심어져 있는 구역의 개수를, 둘째 줄에 오이만 심어져 있는
구역의 개수를, 셋째 줄에 토마토만 심어져 있는 구역의 개수를 출력한다

'''
# 밭이 하나의 작물로 이루어져 있는지 check
# arr: 2차원 배열 / x, y: 검증할 밭의 시작점 / len: 검증할 밭의 길이
def check(arr, x, y, len):
    global ltc, tmt, ccb
    base = arr[x][y]
    checked = True
    for i in range(len):
        for j in range(len):
            if base != arr[x+i][y+j]:
                checked == False
                divide(arr, x, y, len)
                return

    # 각 채소들의 밭의 갯수를 하나씩 더해준다
    if checked == True:
        if base == -1:
            ltc += 1
        elif base == 0:
            ccb += 1
        else :
            tmt += 1

# 밭을 9개로 나누는 함수 divide
# arr: 2차원 배열 / x, y: 나눌 밭의 시작점 / len: 나눠야 할 밭의 길이
def divide(arr, x, y, len):
    mul = int(len/3) # 나눠진 밭의 길이
    xrr = [] # 나눠진 밭들의 시작점 x 좌표
    yrr = [] # 나눠진 밭들의 시작점 y 좌표
    for i in range(3):
        xrr.append(x+i*mul)
        xrr.append(x+i*mul)
        xrr.append(x+i*mul)
    for _ in range(3):
        yrr.append(x+0*mul)
        yrr.append(x+1*mul)
        yrr.append(x+2*mul)
    
    for i in range(9):
        check(arr, xrr[i], yrr[i], mul)



c_len = int(input()) # 밭의 한변의 길이 값
arr = [] # 밭의 채소 값들이 입력될 배열
ltc = 0 # 상추
ccb = 0 # 오이
tmt = 0 # 토마토

for _ in range(c_len):
    line = input()
    arr.append(list(map(int, line.split(' '))))

check(arr, 0, 0, c_len)
print(ltc)
print(ccb)
print(tmt)