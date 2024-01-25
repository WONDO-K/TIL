from hw_1462 import Dog
from hw_1463 import Cat

# 아래 클래스를 수정하시오.
class Pet(Dog,Cat):
    def __init__(self,sound):
        self.sound = sound
    def play(self):
        print('애완동물과 놀기')
    def make_sound(self):
        print(self.sound)

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
