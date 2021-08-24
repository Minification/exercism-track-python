EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.direction = direction
    
    def move(self, instructions):
        for instruction in instructions:
            self._move(instruction)
        
    def _move(self, instruction):
        r = instruction == "R"
        l = instruction == "L"
        if not (l or r):
            south = self.direction == SOUTH
            east = self.direction == EAST
            west = self.direction == WEST
            use_x = west or east
            use_y = not use_x
            sign = -1 if south or west else 1
            self.coordinates = (self.coordinates[0] + sign * use_x, self.coordinates[1] + sign * use_y)
        else:
            self.direction = (self.direction + r + (-1*l) ) % 4
