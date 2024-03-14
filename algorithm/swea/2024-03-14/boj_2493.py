import sys
input = sys.stdin.readline

n = int(input())

# i번째 원소는 i번째 탑의 신호를 수신할 수 있는 탑의 위치
point = [0 for _ in range(n+1)]

arr = [0] + list(map(int,input().split()))

stack = []

for i in range(1,n+1):

    while stack:
        if arr[i]>stack[-1][1]: # 현재 탑이 스택 최상단의 탑 높이보다 크다면 수신 가능한 탑이 없으므로 버림
            stack.pop()
        else: # 현재 탑이 스택 최상단의 탑 높이보다 작다면 수신가능한 위치이므로 저장
            point[i] = stack[-1][0] # 스택 top의 0번 인덱스의 좌표를 저장
            break
    # 현재 좌표, 좌표의 탑 높이
    stack.append([i,arr[i]])

print(*point[1:n+1])