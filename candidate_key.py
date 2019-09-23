'''
2018 카카오 <후보키>
https://programmers.co.kr/learn/courses/30/lessons/42890

방법 
1. 칼럼별로 원소들을 집합으로 만든다. 로우 수와 같으면 후보키.
2. 남은 칼럼들에 대해 가능한 칼럼의 조합을 구한다.
3. 유일성: 유일성을 확인한다.
4. 최소성: 남은 조합 가운데 유일성이 입증된 조합을 제외한다.
'''

# 57.1
from itertools import combinations

def solution(relation):
    answer = 0
    candidate_keys = []
    num_of_columns = len(relation[0])
    num_of_rows = len(relation)
    columns = [x for x in range(0, num_of_columns)]
    
    attributes = []
    
    # 1.
    for c in range(num_of_columns):
        for r in range(num_of_rows):
            attributes.append(relation[r][c])
            att_set = set(attributes)
        if len(att_set) == num_of_rows:
            candidate_keys.append([c])
        attributes=[]

    # 2.
    columns = [x for x in columns if [x] not in candidate_keys]
    cmb_columns = []

    for i in range(1, len(columns)+1):
        tmp = list(combinations(columns, i))
        cmb_columns += tmp

    # 3.
    for i in range(len(cmb_columns)):
        for r in range(num_of_rows):
            tmp = ''
            for j in cmb_columns[i]:
                tmp += relation[r][j]
            attributes.append(tmp)
        att_set = set(attributes)
        if len(att_set) == num_of_rows:
            candidate_keys.append(list(cmb_columns[i]))
        attributes=[]
    
    # 4.
    ans = candidate_keys[:]
    for c in candidate_keys:
        for d in candidate_keys:
            if set(c).issubset(set(d)) and c != d:
                candidate_keys.remove(c)
                break 

    answer = len(candidate_keys)
    return answer


# 통과 (라이브러리 사용)
def solution2(relation):
    answer = 0

    all = list()
    uniqeIndex = []

    if len(relation) > 0:
        # colum의 개수
        colSize = len(relation[0])
        # row의 개수
        rowSize = len(relation)

    # 모든 컬럼의 조합 구하기 (Set형태)
    for i in range(1, colSize+1):
        all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])

    # 조합들의 유일성 검증
    for comb in all:
        vaildSet = set()
        # 조합에 해당되는 로우를 하나의 str로 합쳐서 set에 넣음
        for row in range(rowSize):
            temp = ''
            for col in comb:
                temp += relation[row][col]
            vaildSet.add(temp)
        # 유일성 확인
        if len(vaildSet) == rowSize:
            uniqeIndex.append(comb)

    delSet = set()
    # 최소성 검증
    for min in uniqeIndex:
        for idx, elem in enumerate(uniqeIndex):
            if min.issubset(elem) and min != elem:
                delSet.add(uniqeIndex.index(elem))

    answer = len(uniqeIndex) - len(delSet)
    return answer


# 추천 많은 풀이 (라이브러리 미사용, 비트연산 사용)
def solution3(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)


# 테스트    
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['a','b','c'], ['1','b','c'], ['a','b','4'], ['a','5','c']]))
print(solution([['a','1','4'],['2','1','5'],['a','2','4']]))