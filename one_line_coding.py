'''
투빅스 (5주차 1번)

문제
임채빈은 한 줄 코딩을 좋아한다. 따라서 다음의 파이썬 변수들 만을 이용하여 한 줄 코딩을 하려 한다.
a: 변수
b: 변수
one: 하나의 인자를 갖는 함수
two: 두개의 인자를 갖는 함수
그러나 너무 길게 한 줄 코딩 하다 보니, 인자 개수를 실수하거나, 괄호 실수를 한다. 코딩 고수 임채빈은 이 두 실수 이외의 실수는 하지 않는다.
임채빈을 위해 주어진 코드에 실수가 존재 하는지 안 하는지 판단 하는 프로그램을 짜 주세요.

입력
500자 이하의 코드가 한 줄로 입력된다. 각 함수의 경우 최소 1개, 최대 2개의 인자를 갖는다.
즉, two(a,a,b) 와 같은 입력은 없다. 각 인자는 , 로 구분된다. 즉, two(a, b) 와 같은 입력은
없고 two(a,b) 와 같은 입력만 주어진다. 모든 입력은 적어도 한 번의 함수를 사용한다.

출력
맞는 코드일 경우 No Error, 틀렸을 경우 Syntax Error 를 출력하라.
'''
def wk5_1(): 
    text = input()
    check(text)
    print('No Error' if result['false']==0 else 'Syntax Error')
 
def check(text):
    ONE, TWO = 'one', 'two'
    if len(text) == 1:
        '''
        재귀함수의 종료조건입니다.
        주어진 문자열 값의 길이가 1인 경우(a 또는 b) 종료하도록 설정하였습니다.
        '''
        result['true'] += 1
        return
 
    outer_func = text[:3]   # 사용된 함수 (one or two)
    inner_text = text[4:-1] # 함수 내부의 parameter (괄호 안의 값 - one일 경우 1개, two일 경우 2개)
 
    if not balanced_parenthesis(inner_text): # 괄호의 짝이 맞는지 확인
        '''
        예시 input 중에 괄호 개수가 맞지 않는 경우도 있었습니다.
        재귀함수를 호출하기 전에 괄호 개수로 1차 검증을 하여 불필요한 재귀 연산을 방지하였습니다.
        '''
        result['false'] += 1
        return
    
    param = count_param(inner_text) # 함수 내부의 parameter를 분리 (one일 경우 1개, two일 경우 2개)
    
    # 아래 print문을 함께 출력해서 보시면 재귀의 흐름을 확인할 수 있습니다.
    # print('함수:',outer_func)
    # print('함수 내부:',inner_text)
    # print('함수의 인자:',param)
    # print('---------------')
 
    '''
    미리 파악한 함수의 종류에 따라 조건문을 설정하였습니다.
        one함수의 경우 parameter의 길이가 1일 것이고, 해당 parameter에 대한 재귀를 호출합니다.
        two함수의 경우 parameter의 길이가 2일 것이고, 나뉘어진 각 paramaeter에 대한 재귀를 호출합니다.
    각 함수에 대한 parameter의 개수가 일치하지 않을 경우 false 값을 추가합니다.
    '''
    if outer_func == ONE:     # 각 함수(one, two)에 대한 parameter 개수 확인
        if len(param) == 1:
            check(inner_text) # check(param[0])과 동일한 동작을 합니다.
        else:
            result['false'] += 1
            return
    else:
        if len(param) == 2:
            check(param[0])
            check(param[1])
        else:
            result['false'] += 1
            return
 
def count_param(text): # 주어진 입력값이 몇 개로 구분되는지 판단하는 함수
    '''
    input값이 문자열로 들어오기 때문에 one, two의 parameter 개수를 구분해야 할 필요가 있었습니다.
    그러나 two(a,two(a,one(b))) 처럼 가장 바깥의 two 함수에서 쉼표로 구분되는 ',' 뿐 아니라 내부에도 ','가 존재했습니다.
    우선 input 값으로는 함수: one(), two() 내부의 parameter로 정의하였습니다.
    해당 input은 one일 경우 쉼표가 존재하지 않을 것이고, two일 경우 하나의 쉼표가 존재할 것입니다. (물론 다른 함수 내의 쉼표도 존재합니다.)
    다른 함수 내의 쉼표를 걸러내기 위해 Stack 자료구조를 사용하였습니다.
    파이썬 list를 이용한 Stack 사용법은 https://docs.python.org/ko/3/tutorial/datastructures.html 을 참고해주세요.
    이전에 balanced_parenthesis 함수를 통해 괄호 개수가 맞지 않는 경우를 걸러냈기 때문에 이 함수의 input에 존재하는 괄호는 짝이 맞는 상태입니다.
    제가 사용한 규칙은 다음과 같습니다. 
        1. for문으로 input을 쭉 훑을 때 '('가 나오면 stack으로 사용할 list에 추가한다.
        2. 계속 훑다가 ')'가 나오는 경우 (1번에서 넣었던 열린 괄호의 짝) 가장 최근에 추가하였던 열린 괄호를 pop(삭제) 합니다.
        3. stack에 내용물이 있는 경우(다른 함수 안에 있다는 뜻) 그 뒤로 나오는 ','는 모두 통과시킵니다. => 현재 parameter에 사용되는 쉼표가 아니기 때문
        4. 따라서 stack에 내용물이 없는 상태에서 나오는 ','만이 함수(one, two)의 parameter를 구분하는 기준이 될 것입니다.
                (이는 comma라는 boolean 변수를 사용하여 체크하였습니다.)
    
    올바른 케이스인 경우, one 함수에서는 comma가 존재하지 않을 것이고 two 함수에서는 하나의 comma가 존재할 것입니다. => 올바른 케이스인지에 대한 판단은 이 함수에서 판단X
    따라서 comma가 존재하는 경우 주어진 input을 comma의 인덱스 기준으로 나누고,
        존재하지 않는 경우는 input을 그대로 반환시켰습니다.
    comma의 index를 구할 때는 반복문에서 인덱스를 함께 반환하는 enumerate 기능을 사용하였습니다. (참고: https://wikidocs.net/16045)
    '''
    parenthesis = [] # stack으로 사용될 list
    comma = False    # comma 여부를 판단하는 기준
    divide = -1      # comma가 위치한 인덱스
 
    for idx, a in enumerate(text): # stack을 사용하여 괄호 짝 확인
        if a == '(':
            parenthesis.append(a)
        elif a == ')':
            parenthesis.pop()
        elif len(parenthesis) == 0 and a == ',':
            comma = True
            divide = idx # 쉼표가 위치한 인덱스를 저장
    
    return [text[:divide], text[divide+1:]] if comma else [text]
 
def balanced_parenthesis(text): 
    '''
    주어진 문자열 내에서 여는 괄호와 닫는 괄호의 개수를 비교하여 T/F로 반환하였습니다.
    괄호는 한 쌍을 기준으로 하기 때문에 괄호 개수의 합이 홀수이면 False를 반환합니다.
    '''
    count = text.count('(') + text.count(')')
    return True if count%2 == 0 else False
 
if __name__ == '__main__':
    '''
    two함수의 경우 2개의 parameter에 대해 각각 재귀를 호출하면 오류를 체크하기 힘들다고 판단하였습니다.
    따라서 오류를 체크할 전역 변수 result를 선언하여, 각 재귀에 대한 성공/실패 여부를 기록하기로 하였습니다.
    각 재귀함수를 돌릴 때 false값이 하나라도 있으면 Syntax Error를 의미하기 때문에 결과 판단 시 result['false']의 값으로 판단하였습니다.
    '''
    result = {'true':0, 'false':0}
    wk5_1()