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
def wk5_4():
    NN = int(input())
    land = [[int(elm) for elm in input().split(' ')] for _ in range(NN)] # 한 줄씩 받은 입력값을 NxN 행렬로 만든다.
    check(land)
 
    for count in count_list:
        print(count)
 
def check(land):
    '''
    입력으로 받은 구역에
        같은 작물이 있는 경우, 각 작물이 심어진 구역의 개수 출력
        다른 작물이 있는 경우, 9개의 sub 구역으로 분리
    '''
    if is_same(land): # 같은 작물이 심어졌을 때가 종료조건
        count(land)
    else:            
        for each_3 in split_into_9_lists(land): # 우선 3개의 큰 구역들로 구분된다.
            for each in each_3: # 구분된 큰 구역은 각각 3개의 구역을 포함하고 있다.
                check(each) # 구분된 9개의 각 구역에 재귀 호출
 
def count(land):
    '''
    이 함수의 input으로 주어지는 구역은 모두 같은 원소로 이루어졌습니다.
    따라서 원소의 종류(상추, 오이, 토마토)를 구분하여 전역변수에 그 개수만큼 추가합니다.
    '''
    SANGCHU, OI, TOMATO = -1, 0, 1
    first_elm = land[0][0] # 모두 같은 작물이 심어져 있으니, 첫 번째 원소로 판단
    
    if first_elm == SANGCHU:
        count_list[0] += 1
    elif first_elm == OI:
        count_list[1] += 1
    elif first_elm == TOMATO:
        count_list[2] += 1
    else:
        print('오류')
 
def split_into_9_lists(land): # list를 9개의 sub-list로 분할하여 저장
    '''
    land는 NxN list입니다.
    주어진 구역을 9등분해야하기 때문에 전체 길이의 1/3만큼을 나뉠 구역의 길이로 설정합니다.
    우선 land를 가로로 3등분하였고, 그 후 세로로 3등분하여 별도의 list에 저장하였습니다.
    total = 9, small = 3을 예시로 대입해보시면 이해가 잘 될 것 같습니다.
    결과값은 다음과 같은 형태일 것입니다.
    [
        [ [1구역], [2구역], [3구역] ],
        [ [4구역], [5구역], [6구역] ],
        [ [7구역], [8구역], [9구역] ],
    ]
    '''
    total = len(land)   # 한 구역의 가로 길이
    small = total // 3  # 나뉘어질 구역의 가로 길이
    return [[[row[idx:idx+small] for row in land[mid: mid+small]] for idx in range(0, total, small)] for mid in range(0, total, small)]
 
def is_same(land):
    '''
    입력으로 주어진 구역이 같은 작물로만 이루어졌는지 판단하는 함수입니다.
    구역의 첫 번째 원소를 기준으로 삼아 구역을 돌면서 다른 값이 존재하는 경우 False를 반환합니다.
    '''
    criteria = land[0][0]
    for row in range(len(land)):
        for col in range(len(land)):
            if land[row][col] != criteria:
                return False
    return True
 
if __name__ == '__main__':
    '''
    상추, 오이, 토마토가 심어진 구역의 개수를 체크하는 전역변수 count_list를 설정하였습니다.
    '''
    count_list = [0, 0, 0] 
    wk5_4()