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

# 아이디어: 스택 사용. 
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

def check_mistake_bracket(code):
    b_stack = Stack()
    for c in code:
        if c == '(':
            b_stack.push(c)
        elif c == ')':
            if b_stack.is_empty():
                return True
            else: 
                b_stack.pop()
    if b_stack.is_empty():
        return False
    else:
        return True

def check_mistake_args(code):
    tn = code.count('two(')
    cn = code.count(',')
    if tn != cn:
        return True
    else:
        return False

code = input()

if (check_mistake_args(code) or check_mistake_bracket(code)):
    print("Syntax Error")
else:
    print("No Error")