'''
2018 카카오 <길찾기 게임>
https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3
'''
import sys
sys.setrecursionlimit(10**6) 
#파이썬에서 재귀함수의 최대 깊이는 1000이다. 문제에서 1~10000개의 노드가 주어진다고 했기 때문에 깊이 제한을 바꾼다.

class Tree: #트리 구성하는 클래스
    def __init__(self,dataList):
        #자신의 좌표 data
        self.data=max(dataList,key=lambda x :x[1]) #초기화 파라미터 중 y값이 제일 높은 요소가 root가 됨
        leftList =list(filter(lambda x :x[0] < self.data[0] , dataList)) #루트의 x보다 작으면 루트의 왼쪽 하위 트리
        rightList = list(filter(lambda x :x[0] > self.data[0] , dataList)) #루트의 x보다 크면 루트의 오른쪽 하위 트리

        #왼쪽 하위 노드들
        if leftList != []:
            self.left=Tree(leftList) #재귀
        else :
            self.left=None
        
        #오른쪽 하위 노드들
        if rightList != []:
            self.right=Tree(rightList) #재귀
        else :
            self.right=None
            
def fix(node,postList,preList):
    print("현재노드:", node.data, "후위:", postList, "전위:", preList)
    postList.append(node.data)
    if node.left is not None:
        fix(node.left,postList,preList)
    if node.right is not None:
        fix(node.right,postList,preList)
    preList.append(node.data)
    
def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []
    fix(root,postList,preList)
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,postList)))
    # map(함수, 리스트)는 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아준다.
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,preList)))
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))