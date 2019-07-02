# 내 풀이

def solution(N, stages):
    answer = []
    pass_dic = {}
    stay_dic = {}
    fail_dic = {}
    fail_arr = []

    for i in range(1, N+2):
        pass_dic[i] = 0
        stay_dic[i] = 0
        fail_dic[i] = 0

    for n in stages:
        for x in range(1, n+1):
            pass_dic[x] += 1
        stay_dic[n] += 1

    for l in range(1, N+1):
        if stay_dic[l] == 0 or pass_dic[l] ==0:
            fail_dic[l] = 0
        else:
            fail_dic[l] = stay_dic[l]/pass_dic[l]

    fail_arr = sorted(fail_dic.items(), key=lambda x: x[1], reverse=True) #값으로 정렬. [(ㄱ,ㄴ)] 형태로 결과가 나옴.
    answer = [x[0] for x in fail_arr] #위 결과에서 key만 뽑아서 정렬
    del answer[len(answer)-1] #모두 완료한 경우는 제외

    return answer


# 추천을 많이 받은 다른 사람의 풀이

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage) #내가 count의 존재를 잊어버려서 하나하나 더했다면 아예 갯수를 세 버린다.
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0 #0이 들어올 경우를 처리했다(★)
    return sorted(result, key=lambda x : result[x], reverse=True)