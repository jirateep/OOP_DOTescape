import pprint
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
        self.genarate_map()
        self.print_map()

    def genarate_map(self):
        self.map = [[[0 for col in range(4)]for col in range(self.col)] for row in range(self.row)]
        #self.map = [[[0]*4]*self.col]*self.row
        #print(self.map)
        for i in range(0,self.row):
            for j in  range(0,self.col):
                if i == 0:
                    #print("hi3")
                    self.map[i][j][self.DOOR_UP] = -1
                elif self.map[i-1][j][self.DOOR_DOWN] != 0:
                    #print("hi2")
                    self.map[i][j][self.DOOR_UP] = self.map[i-1][j][self.DOOR_DOWN]
                else:
                    #print("hi")
                    if(not self.three_close_door(i,j)):
                        self.map[i][j][self.DOOR_UP] = self.random_status();
                    else:
                        self.map[i][j][self.DOOR_UP] = 1;

                if i == self.row - 1:
                    self.map[i][j][self.DOOR_DOWN] = -1
                elif self.map[i+1][j][self.DOOR_UP] != 0:
                    self.map[i][j][self.DOOR_DOWN] = self.map[i+1][j][self.DOOR_UP]
                else:
                    if(not self.three_close_door(i,j)):
                        self.map[i][j][self.DOOR_DOWN] = self.random_status();
                    else:
                        self.map[i][j][self.DOOR_DOWN] = 1;

                if j == 0:
                    self.map[i][j][self.DOOR_LEFT] = -1
                elif self.map[i][j-1][self.DOOR_RIGHT] != 0:
                    self.map[i][j][self.DOOR_LEFT] = self.map[i][j-1][self.DOOR_RIGHT]
                else:
                    if(not self.three_close_door(i,j)):
                        self.map[i][j][self.DOOR_LEFT] = self.random_status();
                    else:
                        self.map[i][j][self.DOOR_LEFT] = 1;

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
        print(self.map)
        for i in range(0, self.row):
            str = ' '
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_UP] == -1:
                    str += '_   '
                else:
                    str += '    '
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
                str += ' '
            print(str)
            str = ' '
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_DOWN] == -1:
                    str += '_   '
                else:
                    str += '    '
            print(str)

    def random_status(self):
        i = randint(0, 2)
        print(i)
        if(i == 0):
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
