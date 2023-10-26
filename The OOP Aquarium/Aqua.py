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
        pass

    def print_board(self):
        pass

    def get_board(self):
        pass

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        pass

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        pass

    def print_animal_on_board(self, animal: Animal):
        pass
        

    def delete_animal_from_board(self, animal: Animal):
        pass
        

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        pass

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        pass

    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        pass

    def left(self, a):
        pass

    def right(self, a):
        pass

    def up(self, a):
        pass

    def down(self, a):
        pass

    def next_turn(self):
        """
        Managing a single step
        """
        pass
        self.turn += 1

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        pass

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        pass

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
        pass

    
