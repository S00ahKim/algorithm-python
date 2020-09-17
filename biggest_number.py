'''
프로그래머스
가장 큰 수

문제의 numbers의 원소는 0 이상 1,000 이하입니다. 라는 조건을 통해서 
numbers.sort(key=lambda x" x*3, reverse = True)를 해서 정렬

[6, 10, 2]을 예시로 들면, numbers.sort(key=lambda x" x*3, reverse = True)를 하면,
[666, 101010, 222]가 되고 이를 정렬하면, [666, 222, 101010]이 되어서 결과적으로 [6, 2, 10]의 순서가 된다.

그냥 str 비교를 해도 되지만 이렇게 하는 이유는 30, 3 의 경우 3에 우선 순위를 주기 위함이다.
위와 같이 정렬되는 이유는 문자열 비교연산의 경우엔 
첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교해서
같으면 다음 인덱스도 비교하는 과정을 거치기 때문이다.
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))