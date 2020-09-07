'''
프로그래머스
문자열 압축 (2020 카카오)

"aabbaccc"	        2a2ba3c     7 (1은 생략)
"ababcdcdababcdcd"	2ababcdcd   9
"abcabcdede"	    2abcdede    8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17

1. 앞에서부터 자른다.
2. 남는 것은 그냥 붙인다.
'''
def solution(string):
    answer = []
    for s in range(1, len(string)+1): 
        tmp = [string[i:i+s] for i in range(0, len(string), s)]
        a = ''
        cnt = 1
        while tmp:
            t = tmp[0]
            try:
                if t == tmp[1]:
                    cnt += 1
                    tmp.pop(1)
                else:
                    tmp.pop(0)
                    if cnt == 1:
                        a += t
                    else:
                        a += str(cnt)+t
                        cnt = 1
            except:
                if cnt == 1:
                    a += t
                else:
                    a += str(cnt)+t
                    cnt = 1
                break
        answer.append(len(a))
    return min(answer)

print(solution("abcabcabcabcdededededede")) 

# 추천을 많이 받은 다른 사람의 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])