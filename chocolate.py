'''
투빅스 (5주차 2번)

문제
올해 초등학교에 입학한 유민이는 구구단을 외우는 재미에 푹 빠졌다. 
유민이 담임 선생님은 유민이와 즐겁게 구구단을 외우기 위해 초콜릿을 준비했다. 
구구단 문제를 맞추면, 그 문제까지 연속으로 맞춘 문제의 개수만큼 초콜릿을 준다.
구구단 퀴즈의 결과가 O, X로 주어졌을 때, 
유민이가 받을 수 있는 초콜릿의 총 개수를 출력하는 프로그램을 작성하라.

입력
유민이의 퀴즈 결과가 한 줄로 입력된다. 길이가 0보다 크고80보다 작은 문자열이다. 이 문자열은 O와 X로만 이루어져 있다.

출력
유민이가 받을 수 있는 초콜릿의 총 개수를 출력한다
'''

def get_chocolate(string):
    result = list(string)
    chocolate = 0
    acc = 0

    for r in result:
        if r == 'O':
            acc += 1
            chocolate += acc
        else:
            acc = 0
    return chocolate

print(get_chocolate(input()))