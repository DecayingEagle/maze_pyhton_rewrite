from ast import match_case
import math
import random
import numpy

# Rewritten from scratch (no not from the scratch programming language)
class Grid(object):
    # TODO: Fix bug where the current position is rewritten to a wall

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid_arr = numpy.zeros((grid_size + 2, grid_size + 2))        
        self.dir = 1
        self.n = self.set = self.start = self.end = self.start_pos = self.last_dir = 0
        self.arr = [0, 0, 0]
        self.current_pos = [0, 0]

    def pre_gen(self):
        # generate start and end positions
        self.start = math.ceil(random.random() * self.grid_size)
        self.end = math.ceil(random.random() * self.grid_size)

        print(self.start, self.end) # debug

        # make walls
        for i in range(self.grid_size + 2):
            for j in range(self.grid_size + 2):
                if i == 0 or i == self.grid_size + 1  or j == 0 or j == self.grid_size + 1:
                    self.grid_arr[i][j] = 1

        # set current position one step away from start
        self.current_pos = [self.start, self.grid_size]

        # current position
        self.grid_arr[self.current_pos[0]][self.current_pos[1]] = 2
        # starting position
        self.grid_arr[self.grid_size + 1][self.start] = 3
        # ending position
        self.grid_arr[0][self.end] = 4

        # self.generate_walls(self.current_pos[0], self.current_pos[1])

    def generate_walls(self, x, y):
        # x, y = current position

        # grid_arr:
        # 0 = left
        # 1 = up
        # 2 = right

        # randomly generate 3 sides of walls
        for i in range(len(self.arr)):
            if random.random() < 0.9:
                self.grid_arr[i] = 1
            else:
                self.grid_arr[i] = 0

        # place walls in the grid array
        if self.arr[0] == 1 and x != 1:
            self.grid_arr[x - 1][y] = self.arr[0]
        if self.arr[1] == 1 and y != 1:
            self.grid_arr[x][y - 1] = self.arr[1]
        if self.arr[2] == 1 and x != self.grid_size:
            self.grid_arr[x + 1][y] = self.arr[2]
                
    def generate(self):
        pass
























# ! Depricated, tried to rewrite code straight from javascript
class Grid2(object):
    def __init__(self, grid_size):
        self.grid_size = grid_size
        
        self.grid_arr = [[0 for x in range(self.grid_size + 2)] for y in range(self.grid_size + 2)]
        self.dir = 1
        self.facing = 2
        self.n = self.set = self.start = self.end = self.start_pos = self.last_dir = 0
        self.arr = [0, 0, 0]
        self.current_pos = [0, 0]

    def pre_gen(self):
        self.start = math.ceil(random.random() * self.grid_size)
        self.end = math.ceil(random.random() * self.grid_size)
        print(self.start, self.end)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i == 0 or i == self.grid_size + 1 or j == 0 or j == self.grid_size + 1:
                    self.grid_arr[j][i] = 1
                    if i == self.end and j == 0:
                        self.grid_arr[j][i] = 1
                    if i == self.start and j == self.grid_size + 1:
                        self.grid_arr[j][i] = 1
        self.grid_arr[self.grid_size+1][self.start] = 3
        self.grid_arr[0][self.end] = 2
        self.current_pos = [self.grid_size, self.start]

        for i in range(2):
            if random.random() < 0.95:
                self.arr[i] = 1
            else:
                self.arr[i] = 0 
            
    def generate(self):
        while True:
            # 0 = left turn, 1 = straight, 2 = turn right
            self.dir = math.floor(random.random() * 3) 
            if self.dir != 0 and self.start != 1 or (dir != 2 and self.start != self.grid_size):
                break
            
        for i in range(2):
            if random.random() < 0.95:
                self.arr[i] = 1
            else:
                self.arr[i] = 0

        match(self.dir):
            # facing: 0 = down, 1 = left, 2 = up, 3 = right
            case 0:
                if self.facing != 0: 
                    self.facing -= 1
                else:
                    self.facing = 3
            case 1:
                pass
            case 2:
                if self.facing != 3:
                    self.facing += 1
                else:
                    self.facing = 0
            case _:
                print("Invalid facing direction") # Should never happen

        match(self.facing):
            # facing: 0 = down, 1 = left, 2 = up, 3 = right
            case 0:
                self.grid_arr[self.current_pos[0]][self.current_pos[1] + 1] = self.arr[0]
                self.grid_arr[self.current_pos[0]][self.current_pos[1] - 1] = self.arr[1]

                if self.current_pos[1] < self.grid_size and self.grid_arr[self.current_pos[0]][self.current_pos[1] + 1] != 1:
                    self.current_pos[1] += 1
                    self.grid_arr[self.current_pos[0]][self.current_pos[1]] = 4
                    self.grid_arr[self.current_pos[0] - 1][self.current_pos[1]] = 0
            case 1:
                self.grid_arr[self.current_pos[0]][self.current_pos[1] - 1] = self.arr[0]
                self.grid_arr[self.current_pos[0] - 1][self.current_pos[1]] = self.arr[1]

                if self.current_pos[0] > 1 and self.grid_arr[self.current_pos[0] - 1][self.current_pos[1]] != 1:
                    self.current_pos[0] -= 1
                    self.grid_arr[self.current_pos[0]][self.current_pos[1]] = 4
                    self.grid_arr[self.current_pos[0]][self.current_pos[1] + 1] = 0
            case 2:
                self.grid_arr[self.current_pos[0] - 1][self.current_pos[1]] = self.arr[0]
                self.grid_arr[self.current_pos[0] - 1][self.current_pos[1]] = self.arr[1]

                if self.current_pos[1] >  1 and self.grid_arr[self.current_pos[0]][self.current_pos[1] - 1] != 1:
                    self.current_pos[1] -= 1
                    self.grid_arr[self.current_pos[0]][self.current_pos[1]] = 4
                    self.grid_arr[self.current_pos[0] + 1][self.current_pos[1]] = 0
            case 3:
                self.grid_arr[self.current_pos[0]][self.current_pos[1] + 1] = self.arr[0]
                self.grid_arr[self.current_pos[0] + 1][self.current_pos[1]] = self.arr[1]

                if self.current_pos[0] < self.grid_size and self.grid_arr[self.current_pos[0] + 1][self.current_pos[1]] != 1:
                    self.current_pos[0] += 1
                    self.grid_arr[self.current_pos[0]][self.current_pos[1]] = 4
                    self.grid_arr[self.current_pos[0]][self.current_pos[1] - 1] = 0
            case _:
                print("Invalid direction")
            
    