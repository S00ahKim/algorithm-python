'''
프로그래머스
네트워크
'''

# 15/100
def solution(n, computers):
    connections = dict()
    nets = []

    for i in range(n):
        connections[i] = []
        for j in range(n):
            if computers[i][j] == 1:
                connections[i].append(j)

    for i in range(n):
        tmp = set()
        bc = check(i, nets)
        if bc[0]:
            for item in connections[i]:
                nets[bc[1]].add(item)
        else:
            for x in connections[i]:
                c = check(x, nets)
                if c[0]:
                    nets[c[1]].add(x)
                else:
                    tmp.add(x)
            if len(tmp) != 0:
                nets.append(tmp) 
    return len(nets)

def check(x, nets):
    for net in nets:
        if x in net:
            return (True, nets.index(net))
    return (False, -1)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


# 풀이

def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(0, len(computers)):
            if computers[j][i] ==1 and visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer