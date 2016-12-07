from random import randint

class Map:
    DOOR_UP = 0
    DOOR_DOWN = 1
    DOOR_LEFT = 2
    DOOR_RIGHT = 3

    row = 7
    col = 7
    map = 0

    def __init__(self):
        self.generate_map()
        self.print_map()

    def generate_map(self):
        self.map = [[[0 for col in range(4)]for col in range(self.col)] for row in range(self.row)]
        for i in range(0,self.row):
            for j in  range(0,self.col):
                sequence = self.generate_seq()
                for step in sequence:
                    if step == self.DOOR_UP:
                        self.generate_up_door(i,j)
                    if step == self.DOOR_DOWN:
                        self.generate_down_door(i,j)
                    if step == self.DOOR_LEFT:
                        self.generate_left_door(i,j)
                    if step == self.DOOR_RIGHT:
                        self.generate_right_door(i,j)

    def generate_seq(self):
        seq = []
        i = 0
        while i < 4:
            j = randint(0, 3)
            if not j in seq:
                seq.append(j)
                i += 1
            else:
                continue
        return seq

    def generate_up_door(self, i, j):
        if i == 0:
            self.map[i][j][self.DOOR_UP] = -1
        elif self.map[i-1][j][self.DOOR_DOWN] != 0:
            self.map[i][j][self.DOOR_UP] = self.map[i-1][j][self.DOOR_DOWN]
        else:
            if(not self.three_close_door(i,j)):
                self.map[i][j][self.DOOR_UP] = self.random_status();
            else:
                self.map[i][j][self.DOOR_UP] = 1;

    def generate_down_door(self, i, j):
        if i == self.row - 1:
            self.map[i][j][self.DOOR_DOWN] = -1
        elif self.map[i+1][j][self.DOOR_UP] != 0:
            self.map[i][j][self.DOOR_DOWN] = self.map[i+1][j][self.DOOR_UP]
        else:
            if(not self.three_close_door(i,j)):
                self.map[i][j][self.DOOR_DOWN] = self.random_status();
            else:
                self.map[i][j][self.DOOR_DOWN] = 1;

    def generate_left_door(self, i, j):
        if j == 0:
            self.map[i][j][self.DOOR_LEFT] = -1
        elif self.map[i][j-1][self.DOOR_RIGHT] != 0:
            self.map[i][j][self.DOOR_LEFT] = self.map[i][j-1][self.DOOR_RIGHT]
        else:
            if(not self.three_close_door(i,j)):
                self.map[i][j][self.DOOR_LEFT] = self.random_status();
            else:
                self.map[i][j][self.DOOR_LEFT] = 1;

    def generate_right_door(self, i, j):
        if j == self.col - 1:
            self.map[i][j][self.DOOR_RIGHT] = -1
        elif self.map[i][j+1][self.DOOR_LEFT] != 0:
            self.map[i][j][self.DOOR_RIGHT] = self.map[i][j+1][self.DOOR_LEFT]
        else:
            if(not self.three_close_door(i,j)):
                self.map[i][j][self.DOOR_RIGHT] = self.random_status();
            else:
                self.map[i][j][self.DOOR_RIGHT] = 1;

    def print_map(self):
        #print(self.map)
        for i in range(0, self.row):
            str = ' '
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_UP] == -1:
                    str += '_  '
                else:
                    str += '   '
            print(str)
            str = ''
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_LEFT] == -1:
                    str += '|'
                else:
                    str += ' '
                str += ' '
                if self.map[i][j][self.DOOR_RIGHT] == -1:
                    str += '|'
                else:
                    str += ' '
            print(str)
            str = ' '
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_DOWN] == -1:
                    str += '_  '
                else:
                    str += '   '
            print(str)

    def random_status(self):
        if(randint(0, 1) == 0):
            return 1
        else:
            return -1

    def three_close_door(self,i,j):
        count = 0
        for x in range(4):
            if self.map[i][j][x] == 0:
                count += 1
        if count == 3:
            return True
        return False
