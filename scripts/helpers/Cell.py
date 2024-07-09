class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [1, 1, 1, 1, ]
        self.neighbours = []
        self.visited = False
        self.not_visited_neighbours = 0

    def __repr__(self):
        return repr(f"({self.x}, {self.y})")

    def pos(self):
        return(self.x, self.y)
