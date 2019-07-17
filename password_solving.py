'''
투빅스 (1주차 2번)

문제: 현재 투빅스와 B 모 동아리는 전쟁 중이다. 따라서 양 측은 암호화된 문장으로 통신한다. 
투빅스 정보 보안 담당인 당신은 첩보를 통해 적의 암호 알고리즘과 해당하는 키를 알아냈다. 
암호 알고리즘은 변형된 치환 암호로써 다음과 같다.
단어 P는 항상 소문자 영어로 되어있고, P 의 각 알파벳을 알파벳 순서 기준 한 칸 뒤 알파벳으로 바꾼다. 
알파벳 z 의 경우 마지막 알파벳이므로 a 로 바꾸어진다. 이에 의해 변형된 단어를 P` 라 하자. 
이후 각 P`를 무작위 단어 C 와 대응 시킴으로써 문장을 암호화 한다.
파이썬을 이용한 암호 분석 권위자인 당신이 이 전쟁의 유일한 희망이다. 
N개의 키와 문장이 주어졌을 때, 그 문장을 해석할 수 있는 프로그램을 짜시오. 
문장은 항상 해독 가능하다.

<예시>
P`          C
mpwf        xzvcf
krvz        cv
j           vzcqru
zpv         dfda
가 주어질 경우:
i love you 의 경우 i 는 j, love 는 mpwf, you 는 zpv로 바뀐다. 이 때 각 변형된 단
어들은 위에서 주어진 키들의 대응관계에 의해 치환되므로, 최종적으로
i love you 는 vzcqru xzvcf dfda 로 암호화가 된다.

입력
첫 줄에 N (3 이상 500 이하) 이 주어지고 이어지는 N개의 줄에는 단어 P` 그에 대응되는 단어 C 가 주어진다. 
마지막 줄에는 해독 할 문장이 주어진다. 
각 단어 P` 와 C는 길이가 최대 10이고 중복되어 나타나지 않음이 보장된다. 
해독 할 문장은 최대 500개의 단어를 가지고 있다.

출력
해독 된 문장을 출력한다.
'''

decryption = {}
answer = []

# input
N = int(input())
for i in range(N):
    PnC = input().split(' ')
    decryption[PnC[1]] = PnC[0]
sentence = input().split(' ')

# C -> P`
for i in range(len(sentence)):
    answer.append(decryption[sentence[i]])

# P` -> P
def alphabet_forward(arr):
    answer = []
    for i in range(len(arr)):
        tmp = list(arr[i])
        tmp2 = []
        for j in range(len(tmp)):
            char = chr(ord(tmp[j]) -1)
            if char == '`':
                char = 'z'
            tmp2.append(char)
        answer.append(''.join(tmp2))
    return answer

print(' '.join(alphabet_forward(answer)))