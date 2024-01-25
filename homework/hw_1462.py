from hw_1461 import Animal

# 아래 클래스를 수정하시오.
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def bark(self):
        print('멍멍!')
        
if __name__ == "__main__":
    dog1 = Dog()
    dog1.bark()

# 부모 클래스 생성자가 호출되면 차례로 그를 상속받는 자식들이 차례로 호출되는데
# 동물의 수는 1마리 입니다.
# 동물의 수는 2마리 입니다.
# 위와 같이 실행부분이 계속 실행되어 출력된다.

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# 클래스 정의부만이 아닌 실행하는 코드까지 같이 실행이 되는 거 같은데 해결방법을 모르겠음

# 해결방안 찾았음
# 파이썬은 모듈을 import할 때 import한 모듈 내의 코드가 실행되기 때문에 클래스 정의 부분만 가져올 수 있게 처리해주어야 한다.
# improt시 코드가 실행되지 않게 하려면 모듈이 직접 실행될 때만 실행되도록 하는 조건문인 if __name__ == "__main__":를 꼭 실행 코드에 감싸주어야 한다.

