# 내 풀이
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]
        nth = commands[i][2]-1
        tmp = array[start:end]
        tmp.sort()
        print(start, end, nth, tmp)
        a = tmp[nth]
        answer.append(a)
    return answer

# 추천을 많이 받은 다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))