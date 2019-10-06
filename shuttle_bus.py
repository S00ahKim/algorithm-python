'''
프로그래머스 셔틀버스
https://programmers.co.kr/learn/courses/30/lessons/17678

셔틀 운행 횟수 n, 셔틀 운행 간격 t, 
한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable

1) _시간 _분 형식의 timetable을 전부 분으로 변환한 후 소팅
2) 셔틀이 9시부터 n회 t간격으로 역에 도착하므로 버스가 도착하는 시간에 대한 bustable을 만든다.
3) 버스테이블의 버스 시간대에 대해 해당 시각보다 일찍 또는 딱 맞게 온 승객 리스트를 만든다.
4) 만약 이번 시간대 i가 마지막 셔틀일 경우
   4-1) 승객의 수가 한 셔틀에 탈 수 있는 최대 크루 수보다 같거나 크면 콘이 탈 수 없기 때문에 더 일찍 와야 한다.
   4-2) 승객의 수가 m보다 작으면 콘이 탈 수 있고 딱 맞게 와도 되기 때문에 답은 해당 시간대가 된다.
5) 이번 시간대 i가 마지막 셔틀이 아니고, 승객 수가 m보다 작거나 같을 경우 모두 탈 수 있기 때문에
    timetable에서 태운 승객은 인덱싱해서 날려 준다
6) 이번 시간대 i가 마지막 셔틀이 아니고, 승객 수가 m보다 클 경우 모두 탈 수 없기 때문에
    최대 탑승 가능한 승객 수 만큼만 날려 준다.
7) answer는 분 단위이므로, 시간으로 바꾸어 준다.
    divmod를 하면 (몫, 나머지)를 반환하는데, 60으로 나눈 몫이 시간이므로 [0] 해주고,
    몫이 한 자리수일 경우 앞에 0을 붙이기 위해 rjust(오른쪽 정렬)를 사용한다.
    분도 마찬가지 방법으로 구한다.
'''
def solution(n,t,m,timetable):
    timetable=[int(i[:2])*60+int(i[3:]) for i in timetable]
    timetable.sort()
    bustable=[9*60+t*i for i in range(n)]

    for i in bustable:
        passenger=[p for p in timetable if p<=i]
        if i==bustable[-1]:
            if len(passenger)>=m:
                answer=passenger[m-1]-1
            elif len(passenger)<m:
                answer=i
        elif len(passenger)<=m:
            timetable=timetable[len(passenger):]
        elif len(passenger)>m:
            timetable=timetable[m:]
    answer= str(divmod(answer,60)[0]).rjust(2,'0')+':'+str(divmod(answer,60)[1]).rjust(2,'0')
    return answer

print(solution(10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] ))