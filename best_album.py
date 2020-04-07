'''
프로그래머스
베스트 앨범

풀이
1. 장르별 재생수 카운트
2. 장르별 (플레이시간, 노래번호) 딕셔너리 생성
3. 플레이시간은 높은 순, 노래번호는 낮은 순으로 정렬 (조건이 반대라 뒤에 -1 붙임)
4. 정렬된 3번 리스트에서 노래번호만 answer에 append
'''
import operator

def solution(genres, plays):
    answer = []
    genre_count_dict = dict()
    count_song_dict = dict()

    for idx in range(len(genres)):
        if genres[idx] not in genre_count_dict.keys():
            genre_count_dict[genres[idx]] = plays[idx]
        else:
            genre_count_dict[genres[idx]] += plays[idx]

        if genres[idx] not in count_song_dict.keys():
            count_song_dict[genres[idx]] = []
        count_song_dict[genres[idx]].append((plays[idx], idx))

    sorted_d = dict(sorted(genre_count_dict.items(), key=operator.itemgetter(1),reverse=True))

    for key in sorted_d.keys():
        tmp = sorted(count_song_dict[key], key=lambda x: (x[0], -1 * x[1]), reverse=True)[:2]
        for t in tmp:
            answer.append(t[1])
    return answer
            
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))


# 추천을 많이 받은 다른 사람의 풀이

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
