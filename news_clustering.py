'''
프로그래머스 뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677
'''
# 맞은 문제
def solution(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    str1_set=[]
    str2_set=[]
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            str1_set.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            str2_set.append(str2[i]+str2[i+1])
    summation=len(str1_set)+len(str2_set)
    intersect=0
    for i in str2_set:
        if i in str1_set:
            str1_set.remove(i)
            intersect+=1
    if summation==0:
        return 65536
    else:
        return int(intersect/(summation-intersect)*65536)


# 틀린 문제
def solution(str1, str2):
    # 정제
    str1 = str1.upper()
    str2 = str2.upper()

    # 다중집합 만들기
    str1_set = mulset(str1)
    str2_set = mulset(str2)
        
    cnt = 0
    for o in str1_set:
        if o in str2_set:
            cnt+=1
    if cnt == 0 or (len(str1_set)+len(str2_set)) ==0:
        return 65536
    else:
        answer = int(cnt/(len(str1_set)+len(str2_set)-cnt)*65536)
        return answer

def mulset(string):
    mlst = []
    alphabet = [x for x in range(ord('A'), ord('Z')+1)]

    for i in range(len(string)-1):
        if ord(string[i]) in alphabet and ord(string[i+1]) in alphabet:
            mlst.append(string[i]+string[i+1])
    return mlst

# 이 방법이 아니라 일단 조합을 만들고 제외하는 방법.
# def cleansing(string):
#     alphabet = [x for x in range(ord('A'), ord('Z')+1)]
#     string = string.upper()

#     cln = ''
#     for i in string:
#         if ord(i) in alphabet:
#             cln+=i
#     return cln

# def mulset(string):
#     mlst = []
#     for i in range(len(string)-1):
#         mlst.append(string[i]+string[i+1])
#     return mlst

print(solution("aa1+aa2", "AAAA12"))