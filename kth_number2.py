'''
백준 1300
k번째 수

문제에서 나온대로 곧이곧대로 만들면 시간 초과, 배열이 너무 커져서 메모리 부족
그래서 이진 탐색으로 풀기로 한다.

이진탐색을 위해 왼쪽, 즉 시작점이랑 오른쪽, 즉 끝쪽을 초기화한다.
끝을 k로 두는 이유는 정렬했을때 k번째 수를 알고 싶으니까.

그리고 시작점이 끝점 이하일 동안
반복해서 이진탐색을 하는데,

중앙값mid는 시작, 끝을 더해서 2로 나눠두고 시작한다
이건 그냥 임의의 수를 구한 것이다
아무래도 중간부터 하는게 맨앞이나 맨끝보다 효율적이니까 이렇게 둔다

그리고 문제의 N바이 N 배열안의 원소가
N바이 N 배열이 i행 j열이라고 할때
i행 j열의 요소가 i*j니까

임의의 수 mid에 대해 요소 i*j가 몇개나 작거나 같은지 찾고 싶은 것이다. 
그런데 i는 행이 1~N개 있으니까 그건 고정돼 있고, 
j를 구하려면 i를 이항해서 mid/i 이하인 것을 찾으면 된다

그걸 찾기 위해 for문에서 i행을 (1부터 N까지) 돈다.
j가 N보다 커진다는 건 그냥 전부 다 해당된다는 거라서
N개 모두가 mid보다 작다고 봐주면 되므로
mid보다 작은 수의 개수를 세는 cnt에 그만큼 더해준다.
N보다 j가 작으면 N개 전부다 작은게 아니라
j개만큼 작은거니까 그만큼 더해준다.

그 도는게 끝나고 나서
k보다 cnt가 작다는 건 임의의 수 mid가 k보다 앞에 있다는 거고
이게 파라메트릭 서치 개념이다.
그럼 시작점을 mid다음으로 옮겨준다.

그리고 cnt가 K이상이면
답, 그러니까 자기보다 작거나 같은 수를 k개 갖고 있는 수는 임의의 수였던 mid가 된다.
while문을 종료시키기 위해 right에 mid-1을 해준다.

'''
import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

left=1
right=k
ans = 0
mid = 0

while left <= right:
    mid = (left+right)/2
    cnt=0
    for i in range(1, N+1):
        cnt += min(mid/i, N)
    if cnt < k:
        left = mid+1
    else:
        ans=mid
        right=mid-1 
    print(int(left), int(right), int(mid), int(ans))
    
print(int(ans))