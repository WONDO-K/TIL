import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(130)]

for _ in range(n):
    a,b,c = map(str,input().split())
    #아스키 코드 변경
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)

def recur(node):

    if node == 46: # 아무것도 없을 때
        return
    
    # 부모가 정보를 가지고 자식을 향해 갈 수가 있다. -> 위에서 출력
    print(chr(node),end='') # 방문하기 전에 출력
    
    for nxt in graph[node]:
        recur(nxt)

    # 자식이 부모를 향해 정보를 가지고 간다. -> 아래에서 출력
    print(chr(node),end='') # 방문하고 나서 출력

    # print(chr(node),end='') # 출력 위치에 따라 전위 후위 중위가 바뀜

    # recur(graph[node][0]) # 왼쪽
    # recur(graph[node][1]) # 오른쪽

recur(65)
# ABDCEFG

# -------------
# 순회는 결국 출력이 언제 이루어지느냐의 차이

# 왼쪽을 먼저 탐색하고 있음
# 전위 순회
# 왼쪽으로 가든 오른쪽으로 가든 출발전에 현재 노드를 출력해라

# 후위 순회
# 출발 후 왼쪽 오른쪽 모두 방문했다면 현재 노드 출력

# 중위 순회
# 출력을 가운데에 넣는다
# 왼쪽 방문 후 오른쪽으로 가기전에 현재 노드 출력
# 자식 노드가 2명일 경우는 사용 가능하지만 3명 이상인 경우 사용 불가능
# 이진 트리일 경우만 사용 가능하다