# 내 풀이

def solution(skill, skill_trees):
    imp = 0
    word = list(skill)
    
    for s in skill_trees:
        arr = list(s)
        tmp = []
        for a in arr:
            if a in word:
                tmp.append(a)
        for t in range(len(tmp)):
            if tmp[t] != word[t]:
                imp += 1
                #print(t, '번째', tmp[t], word[t])
                break
    return len(skill_trees)-imp

# 다른 사람의 풀이

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer