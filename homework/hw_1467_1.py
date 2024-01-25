# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self,name:str,age:int):
        try:
            if not name or not age:
                raise ValueError()
            try:
                self.user_data['name'] = name
            except(TypeError):
                print('이름은 문자로 입력해야 합니다.')
            try:
                self.user_data['age'] = age
            except(TypeError):
                print('나이는 숫자로 입력해야 합니다.')
        except ValueError:
            print('사용자 정보가 입력되지 않았습니다.')

    def display_user_info(self):
        if self.user_data:
            print('사용자 정보:')
            print(f'이름: {self.user_data["name"]}')
            print(f'나이: {self.user_data["age"]}')
        else:
            pass

user = UserInfo()
print('이름을 입력하세요 : ',end='')
name = input()

print('나이를 입력하세요 : ',end='')
age = input()
print(name,age)

user.get_user_info(name,age)
user.display_user_info()

    
