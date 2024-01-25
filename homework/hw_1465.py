class Animal:

    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    sound = "멍멍"

    def __init__(self) -> None:
        super().__init__()
    def bark(self):
        print(f'{Dog.sound}')

# 아래 클래스를 수정하시오.
class Cat(Animal):
    sound = "야옹"
    def __init__(self):
        super().__init__()
    def meow(self):
        print(f'{Cat.sound}')

# 아래 클래스를 수정하시오.
# class Pet(Dog,Cat):

#     def __init__(self):
#         super().__init__()

#     def __str__(self) :
#         return f'애완동물은 {self.__class__.sound} 소리를 냅니다.'
    
class Pet(Cat,Dog):
    def __init__(self):
        super().__init__()
    
    def __str__(self) :
        return f'애완동물은 {self.__class__.sound} 소리를 냅니다.'    

pet1 = Pet()
print(pet1)