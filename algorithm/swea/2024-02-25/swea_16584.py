import sys
sys.stdin = open('16584_input.txt')
sys.stdout = open('16584_output.txt', 'w')
#
# #
# def f(i, k, s):  # i-1까지 선택한 원소의 합
#     global min_v
#     if i == k:
#         print(f's:{s}')
#         if min_v > s:
#             min_v = s
#     elif s >= min_v:
#         return
#     else:
#         for j in range(i, k):  # p[i] 자리에 올 원소 p[j]
#             p[i], p[j] = p[j], p[i]  # p[i]<->p[j]
#             f(i + 1, k, s + arr[i][p[i]])
#             p[i], p[j] = p[j], p[i]  # 원상복구
#
#
# for tc in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     p = [i for i in range(n)]
#     min_v = 100
#     f(0, n, 0)  # (시작위치, 총 갯수)
#     print(f'#{tc + 1} {min_v}')


#
#
# for tc in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     min_v = float('inf') # 최소값은 초기 비교시 항상 비교 대상이 최솟값보다 작아야 함으로 양의 무한대로 설정한다
#     select_row = [False]*n
#     solve(select_row,[], 0)
#     print(f'#{tc+1} {min_v}')

def solve(row, col, sum_v):
    global min_v,cnt
    cnt+=1

    if col == n:  # 모든 열에 대한 선택이 완료된 경우
        print(f'sum_v : {sum_v}')
        min_v = min(min_v, sum_v)  # 현재 합계와 최소값을 비교하여 갱신
    else:
        for i in range(n):
            if not row[i]:  # 아직 선택되지 않은 행인 경우
                row[i] = True  # 해당 행을 선택 표시
                solve(row, col + 1, sum_v + arr[i][col])  # 다음 열을 선택하고 재귀 호출
                row[i] = False  # 재귀 호출이 끝난 후 행 선택 해제


for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_v = float('inf')  # 초기 최소값 설정
    selected_row = [False] * n  # 각 행의 선택 여부를 저장하는 배열
    cnt=0
    solve(selected_row, 0, 0)  # 함수 호출
    print(f'cnt : {cnt}')
    print(f'#{tc + 1} {min_v}')