data = {'name': '홍길동'}

try:
    print(data['age'])
except(KeyError):
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)     
# 아래에 코드를 작성하시오.



arr = ['반갑', '하세요', '안녕']
try:
    for i in range(4):
        print(arr.pop())
except(IndexError):
    print(arr)
    print('더이상 pop 할 수 없습니다')
# 아래에 코드를 작성하시오.



word = '3.15'
try:
    print(int(word))
except(ValueError):
    print('정수로 변환 가능한 값을 입력해주세요.')
# 아래에 코드를 작성하시오.
