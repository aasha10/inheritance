from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk")

class dog(animal):
    def move(self):
        print("I can bark")

K = human()
K.move()

R = dog()
R.move()