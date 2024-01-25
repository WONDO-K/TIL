data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

for i in data:
    for j in key_list:
        # i.get(j) => value
        # j => key
        # i.get(j) == None => j라는 키에 값이 없을 경우
        if i.get(j) == None:
            # j라는 키에 'unknown'을 삽입하여 현재 i에 삽입되어 있는 딕셔너리를 수정해준다
            i.setdefault(j,'unknown')
            print(f'{j} 은/는 {i[j]} 입니다.')
        else:
            print(f'{j} 은/는 {i[j]} 입니다.')
    print()

