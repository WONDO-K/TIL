import sys
sys.stdin = open('prim_input.txt')
from heapq import heappush, heappop


def prim(start):
    pq = []
    mst = [0] * v

    # 최소 비용
    sum_point = 0
    
    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리 했음
    # [Prim] 가중치가 낮으면 먼저 나와야함
    # -> 동시에 두 가지의 데이터를 다루어야함
    #       1. class로 만들기
    #       2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq,(0,start))

    while pq:
        point, now = heappop(pq)
        print(f'point : {point}')
        print(now,'/',mst)
        
        # 이미 방문했으면
        if mst[now]:
            continue

        # 방문처리
        mst[now] = 1
        # 누적합 추가
        sum_point += point
        print(f'sum_point : {sum_point}')

        # 갈 수 있는 노드들을 보면서
        for to in range(v):
            # 갈 수 없거나 이미 방문 pass
            if graph[now][to] == 0 or mst[to]:
                continue
            heappush(pq,(graph[now][to],to))
    print(f'최소 비용 : {sum_point}')



v,e = map(int,input().split())
# 인접 행렬로 저장
# -[실습] 인접 리스트로 저장해보기

graph = [[0]*v for _ in range(v)]

for _ in range(e):
    start,end,point = map(int,input().split())

    # arr[3][4]=1 ->[기존] 3->4로 갈 수 있다.
    # [가중치 그래프] arr[3][4] = 31 3->4로 가는데 31이라는 비용이 든다.
    
    # 무방향 그래프이기 때문에 역순도 기록
    graph[start][end] = point
    graph[end][start] = point

prim(0)