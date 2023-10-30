import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 7
        self.height = 3

    def get_animal(self):
        grid = [[" ", "*", "*", "*", " ", " ", "*"],
                ["*", "*", "*", "*", "*", "*", "*"],
                [" ", "*", "*", "*", " ", " ", "*"]]

        if self.directionH == 1:
            for row in grid:
                row.reverse()
        return grid
