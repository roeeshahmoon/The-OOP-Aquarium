import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)

    def __str__(self):
        st = f"The crab {self.name} is {self.age} years old and has {self.food} food"
        return st

    def starvation(self):
        print(f"The crab {self.name} died at the age of {self.age} years\nBecause he ran out of food!")

    def die(self):
         print(f"{self.name} died in good health")


