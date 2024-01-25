from hw_1461 import Animal

# 아래 클래스를 수정하시오.
class Cat(Animal):
    def __init__(self,sound):
        super().__init__()
        self.sound = sound
    def meow(self):
        print(f'{self.sound}!')
        #print("야옹!")

if __name__ == "__main__":        
    cat1 = Cat("야옹")
    cat1.meow()



