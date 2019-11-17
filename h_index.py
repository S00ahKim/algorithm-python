def h_index(citations):
    for h in range(max(citations), 0, -1):
        over_h = 0
        for citation in citations:
            if citation >= h:
                over_h += 1
            if over_h == h:
                return h

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for a in range(1, len(arr)+1):
        ans.append(str(h_index(arr[:a])))
    print(' '.join(ans))