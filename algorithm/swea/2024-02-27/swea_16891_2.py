def check_num(player,deck):
    global result

    for i in deck: # i는 선수의 deck에서 뽑아쓰기 때문에 리스트 안에 있는지 확인할 필요 없음
        if i+1 in deck and i+2 in deck: # i+1,i+2가 있다면 triplet
            return player
        if deck.count(i)>=3: # i의 갯수가 3개 이상이면 run
            return player

for tc in range(int(input())):
    arr = list(map(int,input().split()))
    temp_1 = [] # 1번 선수
    temp_2 = [] # 2번 선수

    result = 0

    for i in range(12):
        if i%2==0:
            temp_1.append(arr[i])
            if len(temp_1)>=3: # 길이가 3이하면 triplet,run 둘다 확인 불가하므로 확인할 필요 없음
                if check_num(1,temp_1)==1: # 승자가 1번이라면
                    result = 1
                    break # 이미 조건을 충족해서 다음 연산이 필요 없다.

        elif i%2==1:
            temp_2.append(arr[i])
            if len(temp_1) >= 3:
                if check_num(2,temp_2)==2: # 승자가 2번이라면
                    result=2
                    break

    print(f'#{tc+1} {result}')