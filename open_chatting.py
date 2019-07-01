# 내 풀이

def solution(record):
    users = {'uid':'name'}
    answer = []
    
    for str in record:
        user = str.split(' ')
        cmd = user[0]
        uid = user[1]

        if cmd == "Leave":
            pass
        else: # enter, change에서만 변화가 일어남
            username = user[2] #Leave의 경우에는 2개 단어만 있어서 이 부분은 index 문제로 여기로 뺌
            if uid in users:
                if username == users.get(uid):
                    pass
                else:
                    users[uid] = username
            else:
                users[uid] = username
    
    for str in record:
        user = str.split(' ')
        username = users.get(user[1])
        if user[0] == "Change":
            pass
        elif user[0] == "Enter":
            msg = username+"님이 들어왔습니다."
            answer.append(msg)
        else:
            msg = username+"님이 나갔습니다."
            answer.append(msg)
            
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


# 추천을 많이 받은 다른 사람의 풀이
# 쓸데없는 변수 저장을 안 하고 필요한 부분만 추가해서 간결하다.

def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer