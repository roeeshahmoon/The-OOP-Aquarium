MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        pass

    def get_food(self):
        pass

    def get_age(self):
        pass

    def dec_food(self):
        pass

    def inc_age(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

    def get_position(self):
        pass

    def set_x(self, x):
        pass

    def set_y(self, y):
        pass

    def starvation(self):
        pass

    def die(self):
        pass

    def get_directionH(self):
        pass

    def set_directionH(self, directionH):
        pass

    def get_alive(self):
        pass

    def get_size(self):
        pass

    def get_food_amount(self):
        pass

    def add_food(self, amount):
        pass

    def get_animal(self):
        pass
