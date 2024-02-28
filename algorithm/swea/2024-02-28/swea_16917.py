import sys
sys.stdin = open('16917_input.txt')
sys.stdout = open('16917_output.txt','w')

for tc in range(int(input())):
    n,m = map(int,input().split())
    package = list(map(int,input().split()))
    truck = list(map(int, input().split()))
    # 무게가 무거운 순, 적재 가능 무게가 무거운 순으로 정렬하여 가장 무거운 화물을  실을 수 있는 트럭부터 찾는다.
    package.sort(reverse=True)
    truck.sort(reverse=True)

    package_idx = 0
    truck_idx = 0
    sum_v = 0
    
    while package_idx<n and truck_idx<m:
        # if package_idx>=n or truck_idx>=m: # 화물, 트럭 둘중 하나라도 끝에 도달하면 더이상 옮길 화물이 없거나 트럭이 없다는 의미
        #     break

        if truck[truck_idx]>=package[package_idx]: # 트럭의 적재 가능 무게가 화물의 무게보다 크거나 같을 경우 적재
            sum_v+=package[package_idx]
            package_idx+=1 # 다음 화물과 다음 트럭을 비교한다.
            truck_idx+=1
        else: # 트럭의 적재 가능 무게가 화물의 무게보다 작을 경우 적재 불가능하므로 화물 idx를 증가시켜 적재 가능한 무게까지 이동한다.
            package_idx+=1
    print(f'#{tc+1} {sum_v}')