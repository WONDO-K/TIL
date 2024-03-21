import sys
sys.stdin = open('prim_input.txt')

# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
# -> 코드로 구현 : 전체 간선 정보를 저장 + 가중치로 정렬

# 2. 방문 처리
#   -> 이때, 싸이클 발생하면 안된다.
#   -> 싸이클 여부?? ==>? union-find 알고리즘 활용

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x==y:
        return
    if x<y:
        parents[y] = x
    else:
        parents[x] = y

v,e = map(int,input().split())

# 인접 리스트
edges = [] # 간선 정보들 저장

for _ in range(v):
    start,end,point = map(int,input().split())
    edges.append([start,end,point])

edges.sort(key=lambda x : x[2]) # 가중치를 기준으로 정렬
parents = [i for i in range(v)] # 대표자 배열(자기 자신을 바라봄)
cnt=0
sum_point = 0

# 간선들을 모두 확인
for s,e,p in edges:
    # 싸이클이 발생하면 pass
    # -> 이미 같은 집합에 속해 있다면 pass
    if find_set(s) == find_set(e):
        print(s,e,p,' / 싸이클 발생! 탈락!')
        continue
    print(s,e,p)
    cnt+=1
    # 싸이클이 없으면, 방문처리
    union(s,e)
    sum_point += p

    if cnt == v-1: # mst 완성, 간선의 개수 == v-1
        break
print(f'min cost : {sum_point}')

