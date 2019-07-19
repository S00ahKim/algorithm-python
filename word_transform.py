# BFS: 단어들을 여러 번 비교해야 하기 때문에 순회가 필요하다.

# 양방향에서 데이터를 처리할 수 있는 큐 (알파벳을 하나씩 바꿔가는 단어를 표시해둠)
from collections import deque as queue

# 알파벳이 하나만 다른 단어에 대해 True 리턴
transistable = lambda a, b: sum((1 if x != y else 0) for x, y in zip(a, b)) == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    q, d = queue(), dict()
    q.append((begin, 0))

    # 단어 비교
    d[begin] = set(filter(lambda x: transistable(x, begin), words))

    # 하나씩 차이나는 단어 체크
    for w in words:
        d[w] = set(filter(lambda x: transistable(x, w), words))

    while q:
        cur, level = q.popleft() #단어 cur, 변환 과정의 횟수 level

        # 전부 탐색해도 목표 단어를 만들지 못함 or 단어의 소비가 끝남에도 목표 단어 못 만듦
        if level > len(words):
            return 0

        # 단어를 채운 큐를 목표 단어를 만들 때까지 탐색
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))