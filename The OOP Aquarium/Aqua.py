import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []

    def build_tank(self):
        for i in range(self.aqua_height):
            if i == 2:
                self.board[i] = ['|'] + ['~'] * (self.aqua_width - 2) + ['|']
            elif i == self.aqua_height - 1:
                self.board[i] = ['\\'] + ['_'] * (self.aqua_width - 2) + ['/']
            else:
                self.board[i] = ['|'] + [' '] * (self.aqua_width - 2) + ['|']

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def get_board(self):
        return self.board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        if isinstance(animal, Crab.Crab):
            for a in self.anim:
                if isinstance(a, Crab.Crab):
                    if animal.x + 7 == a.x and (animal.directionH == 1 and a.directionH == 0):
                        animal.directionH = 0
                        a.directionH = 1
                        return True

                    elif animal.x - 7 == a.x and (animal.directionH == 0 and a.directionH == 1):
                        animal.directionH = 1
                        a.directionH = 0
                        return True

    def print_animal_on_board(self, animal: Animal):
        for row in range(animal.height):
            for col in range(animal.width):
                self.board[animal.y + row][animal.x + col] = animal.get_animal()[row][col]

    def delete_animal_from_board(self, animal: Animal):
        self.anim.remove(animal)

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        if fishtype == 'sc':
            fish = Scalar.Scalar(name, age, x, y, directionH, directionV)
        if fishtype == 'mo':
            fish = Moly.Moly(name, age, x, y, directionH, directionV)
        if fish.y + fish.height > self.aqua_height - MAX_CRAB_HEIGHT:
            return False
        if not self.check_if_free(fish.x, fish.y):
            return False
        self.anim.append(fish)
        self.print_animal_on_board(fish)
        return True

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        if crabtype == 'oc':
            crab = Ocypode.Ocypode(name, age, x, y, directionH)
        if crabtype == 'sh':
            crab = Shrimp.Shrimp(name, age, x, y, directionH)
        if not self.check_if_free(crab.x, crab.y):
            return False
        self.anim.append(crab)
        self.print_animal_on_board(crab)
        return True

    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        try:
            if self.aqua_height - y - 1 <= MAX_CRAB_HEIGHT:
                for row in range(self.aqua_height - y - 1):
                    for col in range(MAX_ANIMAL_WIDTH):
                        if self.board[y + row][x + col] == "*":
                            return False
            else:
                for row in range(MAX_ANIMAL_HEIGHT):
                    for col in range(MAX_ANIMAL_WIDTH):
                        if self.board[y + row][x + col] == "*":
                            return False
            return True
        except IndexError:
            return False

    def left(self, a):
        if a.x == 1:
            a.directionH = 1
        else:
            a.left()

    def right(self, a):
        if a.x == self.aqua_width - a.width - 1:
            a.directionH = 0
        else:
            a.right()

    def up(self, a):
        if a.y == WATERLINE:
            a.directionV = 0
        else:
            a.up()

    def down(self, a):
        if a.y == self.aqua_height - MAX_CRAB_HEIGHT - a.height - 1:
            a.directionV = 1
        else:
            a.down()

    def next_turn(self):
        """
        Managing a single step
        """
        self.build_tank()
        self.turn += 1
        for animal in self.anim:
            if self.turn % 10 == 0:
                animal.dec_food()
            if self.turn % 100 == 0:
                animal.inc_age()
            if animal.age == 120:
                animal.die()
            if animal.food == 0:
                animal.starvation()
            if not animal.get_alive():
                self.delete_animal_from_board(animal)
        for animal in self.anim:
            self.is_collision(animal)
            if animal.directionH == 0:
                self.left(animal)
            else:
                self.right(animal)
            if isinstance(animal, Fish.Fish):
                if animal.directionV == 0:
                    self.down(animal)
                else:
                    self.up(animal)
        for animal in self.anim:
            self.print_animal_on_board(animal)

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for animal in self.anim:
            print(animal)

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for animal in self.anim:
            animal.add_food(FEED_AMOUNT)

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        """
        steps = 0
        while not 1 <= steps:
            try:
                steps = int(input('How many steps do you want to take?'))
            except ValueError:
                continue
        for n in range(steps):
            self.next_turn()

