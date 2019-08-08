# 테스트 케이스만 통과한 풀이
# 알파벳별 거리를 미리 구해두는 것까지는 했지만 name 중간에 A 문자열이 많아서 중간에 되돌아왔다가 뒤로 돌아가는 경우를 고려하지 못함
def solution(name):
    distances = []
    for i in range(ord("Z")-ord("A")+1):
        if i < (ord("Z")-ord("A")+1)/2:
            distances.append(i)
        elif i == (ord("Z")-ord("A")+1)//2:
            distances.append(i)
        else:
            distances.append(distances[i-1] -1)
    answer = 0
    for i in name:
        answer += distances[ord(i) - ord("A")]

    return answer + len(name) -1

# 올바른 풀이
# 그리디 알고리즘을 적용: 왼쪽으로만 가는 것, 오른쪽으로만 가는 것, 섞어서 이동하는 것 중 최단 거리
def solution(name):
    result=0
    if len(name)==1:#글자 하나면
        if ord(name[0])-ord('A')>13:#알파벳 거리 차이가 14이상이면
            return 26-(ord(name[0])-ord('A'))#알파벳 바꾸기
        else:
            return ord(name[0])-ord('A')
    for i in range(1,len(name)):#왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 이동
        if name[i]!='A':#오른쪽으로 이동 시 A가 아닌 문자의 마지막 위치
            rightDist=i
            print('rightDist',rightDist)
        if name[-i]!='A':
            leftDist=i
            print('leftDist',leftDist)
        if ord(name[i])-ord('A')>13:
            result+=26-(ord(name[i])-ord('A'))#알파벳 바꾸기
            print(name[i],result)
        else:
            result+=ord(name[i])-ord('A')
            print(name[i],result)
    if ord(name[0]) - ord('A') > 13:
        result += 26 - (ord(name[0]) - ord('A')) # 알파벳 바꾸기
        print('0번째',name[0])
    else:
        result+=ord(name[0]) - ord('A')
        print('0번째',name[0])
    dist=min(rightDist, leftDist)
    for i in range(1,(len(name)-1)//2+1):
        if name[i]!='A':
            rightDist=i
        if name[-i]!='A':
            leftDist=abs(-i)
    if rightDist>=leftDist:
        dist=min(dist,2*leftDist+rightDist)
    else:
        dist=min(dist,2*rightDist+leftDist)
    print(result,dist)
    return result + dist

# 그 외 간단한 풀이
# 나처럼 미리 알파벳별 거리를 구해 두긴 했는데 보다 간단하고, max로 그리디를 간편하게 구현
def solution(name):
    updown = list(range(14)) + list(range(12,0,-1))
    updown = {chr(65+k):v for k, v in enumerate(updown)}
    name = [updown[x] for x in name]
    right = 0
    left = 0
    for i in range(len(name)-1):
        if name[1+i] != 0:
            break
        right += 1
    for i in range(len(name)-1):
        if name[-i-1] != 0:
            break
        left -= 1
    return sum(name) + len(name) - 1 - max(left, right)