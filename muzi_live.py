'''
프로그래머스 무지의 먹방 라이브
https://programmers.co.kr/learn/courses/30/lessons/42891

해설:
1초 지날 때마다 하나씩 음식을 확인해가며 시행을 하면 정확성 풀이는 풀리지만, 효율성 풀이는 시간초과로 실패가 뜹니다. 
과거에 경우의 수를 줄이기 위해, 문자열 배열을 미리 사전식으로 정렬한 뒤 비교 연산했던 것처럼 
여기서도 food_times를 미리 정렬해놓습니다. 
예로 주어진 [3, 1, 2]를 정렬하면 s_times는 [1, 2, 3]이 됩니다. 
food_times의 길이를 l_times라고 했을 때, 몇 회를 순회할 것인지를 먼저 구합니다. 
index가 0일 때는 l_time-0의 길이를 s_time[0]번 순회하기 때문에 
전체 시간인 d_time에 s_times[0]*(l_times-0)만큼을 추가해줍니다. 

이후 index에서는 l_times-idx-1만큼의 길이를 s_times[idx]-s_times[idx-1]번 순회하기 때문에 
d_time에 (s_times[1]-s_times[0])*(l_times-1)만큼 추가됩니다. 
이 시행을 d_time이 k보다 클때까지 시행을 반복합니다. 
혹시 d_time이 k보다 커지지 않았는 데 for loop가 끝난다면, 
모든 음식을 다 먹었음에도 시간초가 남았다는 뜻이므로 -1을 return합니다.

현재 상황에서 d_time이 k보다 크다는 것은 목표 시행을 지났다는 뜻이므로 
현재 시행에서 '거꾸로' 답을 찾아갑니다.

마지막으로 먹었던 음식들의 인덱스 배열을 뒤에서부터 lst에 저장하고, 나머지 연산을 통해 타겟을 찾습니다. 
하지만 이렇게만 생각하고 끝나면 특정 테스트 케이스에서 런타임 에러가 뜰 것입니다. 
food_times가 [2, 2, 2]같이모든 음식의 시간이 같은 경우, 
마지막으로 먹었던 음식들의 인덱스 배열이 0이 되어 0으로 나누는 경우가 생기게 됩니다. << **
따라서 이 경우만 예외로 빼서 목표 시간을 나머지 연산하면 문제는 해결됩니다.

출처: https://geonlee.tistory.com/67
'''
def solution(food_times, k):
    s_times = sorted(food_times)
    l_times = len(food_times)
    d_time = 0
    l_idx = 0
    for idx in range(l_times):
        if idx == 0:
            d_time += s_times[idx]*(l_times - idx)
        else:
            d_time += (s_times[idx]-s_times[idx-1])*(l_times - idx)
        if d_time > k:
            l_idx = idx -1
            break
    if d_time <= k:
        return -1
    lst = []
    for idx in range(l_times-1, -1, -1):
        if food_times[idx] > s_times[l_idx]:
            lst.append(idx+1)
    if len(lst) != 0:
        # 초과한 양만큼 뒤에서 순서를 세서 음식을 구함.
        return lst[(d_time - k -1) % len(lst)]
    else:
        # 모든 음식의 번호가 같은 경우, 전체에서 나머지 연산을 해서 결과를 구함.
        return k % l_times+1


# 추천을 많이 받은 다른 사람의 풀이
def solution(food_times, k):
    food_times_dic = {}
    food_times_list = []
    totalTime = 0

    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])

    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    # print k
    # print delTime
    while delTime < k:
        k-=delTime
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i)
        # print k, delTime
        i+=1

    food_times_list = sorted(food_times_list[i-1:], key=lambda x:x[0])
    # print food_times_list
    # print k
    return food_times_list[k%len(food_times_list)][0]+1


# 정확성 효율성 모두 틀림 ㅠㅠ
def solution(food_times, k):
    end = len(food_times)
    idx = 0
    time = 0
    while True:
        if idx == end:
            idx = 0
        if food_times[idx] == 0:
            pass
        else:
            food_times[idx] -= 1
            time += 1
        idx += 1
        if time == k:
            if idx == end:
                idx = 0
            if sum(food_times) != 0:
                answer = idx+1
            else:
                answer = -1
            break
    return answer

print(solution([3,1,2],5)) #1