# import sys
# input = sys.stdin.readline
#
# arr = input().strip().split('-')
# result=0
# for i in range(len(arr)):
#     if '+' in arr[i]:
#         arr[i] = sum(list(map(int,arr[i].split('+'))))
#     if result==0:
#         result+=int(arr[i])
#     else:
#         result-=int(arr[i])
# print(result)
#
#
import sys
input = sys.stdin.readline

arr = input().strip().split('-')
result=0

# -로 나누지만 -가 없이 +로만 구성 될 수 있기 때문에 가장 처음 위치한 문자열을 +로 한 번더 나눈 문자열을 반복문 변수 i에 대입한다.
# 초기 값은 더해야 하기 때문에 result에 i를 더해준다
for i in arr[0].split('+'):
    result+=int(i)

# 이후에 위치할 문자들은 -와 +만 남아 있지만 -는 앞에서 다 걸러졌기 때문에 모두 +로 나눈 다음 모든 원소를 result에서 빼주면 된다.
for i in arr[1:]:
    for j in i.split('+'):
        result-=int(j)
print(result)





