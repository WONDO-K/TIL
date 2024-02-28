import sys
sys.stdin = open('1244_input.txt')
sys.stdout = open('1244_output.txt','w')

for tc in range(int(input())):
    num,cnt = input().split()
    length = len(num)
    cnt = int(cnt)
    before = set([num]) # 3. trans가 set이기 때문에 동일한 타입의 set이 필요함
    trans = set() # 1. 중복이 생김 -> 입력 받는 숫자에 같은 번호가 있을 시 같은 숫자가 되기 때문에 중복 걸러야함

    for _ in range(cnt):
        while before:
            temp = list(before.pop())
            for i in range(length-1):
                for j in range(i+1,length): # 0번 인덱스를 1~n 까지의 숫자들과 바꾼후 비교해야함
                    temp[i],temp[j] = temp[j], temp[i]
                    print(f'temp : {temp}')
                    trans.add(''.join(temp))
                    temp[i], temp[j] = temp[j], temp[i]
        trans,before = before,trans # 2. 백트래킹 후의 결과를 토대로 다음 숫자를 변경해야함/ before가 비었기 때문에 버려야함
    print(trans)
    print(before)
    print(f'#{tc+1} {max(before)}')

