# 내 풀이

def solution(a, b):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    # a 달의 1일의 요일을 알아낸다
    firstday = find_first_day(a)
    
    # b-1/7 의 나머지가 0이면 1일인 요일, 아니면 나머지만큼 요일 +
    idx = firstday + ((b-1)%7)
    idx = idx%7
    return weekday[idx]

def find_first_day(a): #31일이 연속해서 두 번 나오는 부분을 고려하지 않아서 초반에 다른 값이 나옴
    for i in range(1, a+1):
        if i == 1:
            fday = 4
        elif i == 3:
            fday += 1
        elif i in [5,7,10,12]:
            fday += 2
        elif i in [2,4,6,8,9,11]:
            fday += 3
        
    fday = fday % 7
    return fday

# 추천을 많이 받은 다른 사람의 풀이

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
