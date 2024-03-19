import sys

sys.stdin = open('2819_input.txt')
sys.stdout = open('2819_output.txt', 'w')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def sol(x,y,nums):
    global cnt, result

    if len(nums) == 7:
        result.add(nums)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            temp = nums # 초기 값 저장
            nums = nums + str(arr[nx][ny])
            sol(nx,ny,nums)
            nums = temp # 초기화


for tc in range(int(input())):
    arr = [list(map(int,input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            nums = str(arr[i][j])
            sol(i,j,nums)
    print(f'#{tc+1} {len(result)}')