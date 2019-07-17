'''
투빅스 (1주차 1번)

문제: 한재연은 숫자 9를 싫어한다. 여러 개의 숫자가 한 줄로 주어 질 때, 자릿수에 9가 들어간 숫자를 제외 한 숫자들 중 N 번째 숫자의 제곱을 구하세요. 
만약 답이 존재하지 않는 경우 문제를 잘못 출제한 한재연에게 항의의 의미로 9를 9개 출력하세요.

입력
첫째 줄에 N (1 이상 100 이하)이 주어지고 다음 줄에 -1000 이상 1000 이하의 정수가 최소 1개부터 최대 100개까지 공백을 구분하여 주어진다.

출력
해당 하는 답을 출력한다
'''

def no_nine(array):
    no_nine_list = []
    for i in range(len(array)):
        if '9' not in array[i]:
            no_nine_list.append(array[i])
    return no_nine_list

N= int(input())
arr_without_nine = no_nine(input().split(' '))

if len(arr_without_nine) >= N:
    print(int(arr_without_nine[N-1])**2)
else:
    print('9'*9)