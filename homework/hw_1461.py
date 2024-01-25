# 아래 클래스를 수정하시오.
class Animal:

    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    # 부모의 생성자를 호출한다.
    def __init__(self):
        super().__init__()


class Cat(Animal):

    def __init__(self):
        super().__init__()

class Pet(Dog,Cat):

    def __init__(self):
        super().__init__()

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

# 파이썬은 모듈을 import할 때 import한 모듈 내의 코드가 실행되기 때문에 클래스 정의 부분만 가져올 수 있게 처리해주어야 한다.
# improt시 코드가 실행되지 않게 하려면 모듈이 직접 실행될 때만 실행되도록 하는 조건문인 if __name__ == "__main__":를 꼭 실행 코드에 감싸주어야 한다.
if __name__ == "__main__":
    dog = Dog()
    print(Pet.access_num_of_animal())
    cat = Cat()
    print(Pet.access_num_of_animal())
