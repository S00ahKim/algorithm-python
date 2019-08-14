'''
투빅스 (5주차 3번)

문제
투빅나라를 다스리는 혜민왕에겐 7명의 충직한 장군이 있다. 그런데 어느 날 혜민왕에게 위기가 찾아왔다. 
변방을 정찰하고 돌아온 장군이 7명이 아닌 9명이었던 것이다. 투빅나라를 침략할 계획을 세우던 이웃나라 소라왕이 2명의 스파이를 심은 것이다. 
9명의 장군은 모두 자신이 투빅나라의 장군이라고 주장했다.
뛰어난 수학적 직관력을 가지고 있던 혜민왕은, 다행스럽게도 일곱 장군의 손바닥 길이의 합이 100이 됨을 기억해냈다. 
9명 장군의 서로 다른 손바닥 길이가 주어졌을 때, 혜민왕을 도와 일곱 장군을 찾는 프로그램을 작성하라.

입력
9개의 줄에 걸쳐 각 장군들의 손바닥 길이가 주어진다. 주어진 손바닥 길이는 100을 넘지 않는 자연수이며, 9명 장군의 손바닥 길이는 모두 다르다.
가능한 정답이 여러 가지인 입력은 주어지지 않는다.

출력
일곱 장군의 손바닥길이를 오름차순으로 출력한다. 일곱 장군을 찾을 수 없는 경우는 없다. 
'''
def find_seven_generals():
    palms = []
    tmp = []
    done = False

    for i in range(9):
        palms.append(int(input()))
    
    for i in range(0,8):
        if done == True:
            break
        for j in range(i+1,9):
            tmp = palms[0:i]+palms[i+1:j]+palms[j+1:9]
            if sum(tmp) == 100:
                tmp.sort() #sort는 재할당하면 None 반환
                done = True #이중 for 문 break 하기 위한 지표
                break
            else:
                tmp = []
    
    return tmp #return에 tmp.sort()하면 None 반환

generals = find_seven_generals()
for g in generals:
    print(g)