'''
백준 1620
나는야 포켓몬 마스터 이다솜
'''

# 시간 초과
# 인풋이 균일하게 들어가지 않아서 그런 듯

N, M = map(int, input().split())
po_dict = {}
num_dict = {}

# po_dict 초기화
for i in range(ord('A'), ord('Z')+1):
    po_dict[i] = []

# num_dict 초기화
for i in range(ord('1'), ord('9')+1):
    num_dict[i] = []

# dict 구성
for n in range(1, N+1):
    tmp = input()
    po_dict[ord(tmp[0])].append((tmp, n))
    num_dict[ord(str(n)[0])].append((n, tmp))

# 답 출력
answer = []
for m in range(M):
    x = input()
    if ord(x[0]) in po_dict.keys():
        for p in po_dict[ord(x[0])]:
            if x == p[0]:
                answer.append(p[1])

    if ord(x[0]) in num_dict.keys():
        for n in num_dict[ord(x[0])]:
            if int(x) == n[0]:
                answer.append(n[1])

for a in answer:
    print(a)

#=======================================================
'''
파이썬은 동적 변수이지만 변수 형태로 저장하기 위해 input()내에서 가공을 하는데, 
raw_input() 은 문자열을 반환하고 
input() 은 raw_input() 을 evaluate한 결과를 반환합니다.

sys.stdin.readline() 은 한 줄의 문자열를 반환하는데 
이것을 int() 로 묶어서 정수로 변환하는게 더 빠른가봅니다.

다른 언어에도 똑같은 원리가 적용되지요.
Java에서는 Scanner 보다 Buffered~ 가 더 처리가 가볍고, 
C++에서는 cout 보다 printf 를 이용하는게 시간적인 측면에서 효율적입니다.

출처 https://www.acmicpc.net/board/view/855
'''
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
pkmn = [] # 포켓몬 이름을 저장할 list (굳이 딕셔너리로 나눠 저장하지 않아도 됨!!)
pkmn_dic = {} # 포켓몬 이름에 따른 번호를 저장할 dictionary
 
for i in range(n) :    
    pk = input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1
 
for _ in range(m):
 
    query = input().rstrip()
 
    # query가 숫자이면 list에서 조회 후 출력
    if query.isdigit() :
        print(pkmn[int(query)-1])
    # query가 문자열이면 dictionary에서 조회 후 출력
    else :
        print(pkmn_dic[query])