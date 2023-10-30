import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3
        self.y = y - self.height -1

    def get_animal(self):
        grid = [["*", " ", "*", " ", " ", " ", " "],
                [" ", "*", "*", "*", "*", "*", "*"],
                [" ", " ", "*", " ", "*", " ", " "]]

        if self.directionH == 1:
            for row in grid:
                row.reverse()
        return grid
