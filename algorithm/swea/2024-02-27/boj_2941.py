import sys
input = sys.stdin.readline

arr = input().rstrip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    arr = arr.replace(i,'*') # 크로아티아 알파벳에 해당하는 문자를 한개로 변경해주고 그 숫자를 출력하면 된다.
print(len(arr))


