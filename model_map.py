from random import randint

class Map:
    DOOR_UP = 0
    DOOR_DOWN = 1
    DOOR_LEFT = 2
    DOOR_RIGHT = 3

    def __init__(self,world):
        self.row = 3
        self.col = 3
        self.num_of_key = 2
        self.world = world
        self.make_new_map()

    def make_new_map(self):
        self.generate_map()
        self.print_map()
        self.insert_key()
        self.insert_gate()
        self.generate_enermy()


    def generate_enermy(self):
        self.enermy = [[0 for col in range(self.col)]for row in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if not [i,j] in self.keys:
                    if not [i,j] == [self.gate_x,self.gate_y]:
                        if not [i,j] == [self.world.player.room_position_x,self.world.player.room_position_y]:
                            blue_enermy = randint(1,5) + self.world.level
                            green_enermy = randint(0,3) +  self.world.level
                            self.enermy[i][j] = [blue_enermy,green_enermy]
        print(self.enermy)

    def insert_key(self):
        self.keys = []
        self.keys_status = [True for i in range(self.num_of_key)]
        i = 0
        while i != self.num_of_key:
            key_x = randint(0,self.row-1)
            key_y = randint(0,self.col-1)
            pos = [key_x,key_y]
            if i == 0 or(not(pos in self.keys) and not (pos == [0,0])):
                self.keys.append(pos)
                i += 1
        print(self.keys)

    def insert_gate(self):
        check = True
        while(check):
            self.gate_x = randint(0,self.row-1)
            self.gate_y = randint(0,self.col-1)
            if not [self.gate_x, self.gate_y] in self.keys and not([self.gate_x, self.gate_y] == [0,0]):
                check = False
        print(self.gate_x,self.gate_y)

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
                if self.check_close_door(i,j,4):
                    self.clear_right(i,j)
        #self.print_map()
        #print()
        self.check_map_available()
        #self.print_map()

    def check_map_available(self):
        available_map = [[0 for col in range(self.col)] for row in range(self.row)]
        self.recure_check(available_map,0,0)
        #print(available_map)
        while not self.check_all_available(available_map):
            self.add_door(available_map)
            #hi = input()
            #self.print_map()
            #print(available_map)
            available_map = [[0 for col in range(self.col)] for row in range(self.row)]
            self.recure_check(available_map,0,0)

    def recure_check(self, available_map, i, j):
        available_map[i][j] = 1
        #print(i,j)
        if i != self.row - 1:
            if available_map[i+1][j] != 1 and self.map[i][j][self.DOOR_DOWN] == 1:
                #print("down")
                self.recure_check(available_map, i+1, j)
        if i != 0:
            if available_map[i-1][j] != 1 and self.map[i][j][self.DOOR_UP] == 1:
                #print("up")
                self.recure_check(available_map, i-1, j)
        if j != self.col - 1:
            if available_map[i][j+1] != 1 and self.map[i][j][self.DOOR_RIGHT] == 1:
                #print("right")
                self.recure_check(available_map, i, j+1)
        if j != 0:
            if available_map[i][j-1] != 1 and self.map[i][j][self.DOOR_LEFT] == 1:
                #print("left")
                self.recure_check(available_map, i, j-1)

    def add_door(self, available_map):
        for i in range(self.row):
            for j in range(self.col):
                if available_map[i][j] == 0:
                    #print(str(i)+" "+str(j))
                    seq = []
                    if i != 0:
                        seq.append(0)
                    if i != self.row - 1:
                        seq.append(1)
                    if j != 0:
                        seq.append(2)
                    if j != self.col - 1:
                        seq.append(3)
                    #print(len(seq)-1)
                    k = randint(0,len(seq)-1)
                    if seq[k] == self.DOOR_UP:
                        #print("here0")
                        self.map[i][j][self.DOOR_UP] = 1
                        self.map[i-1][j][self.DOOR_DOWN] = 1
                    if seq[k] == self.DOOR_DOWN:
                        #print("here1")
                        self.map[i][j][self.DOOR_DOWN] = 1
                        self.map[i+1][j][self.DOOR_UP] = 1
                    if seq[k] == self.DOOR_LEFT:
                        #print("here2")
                        self.map[i][j][self.DOOR_LEFT] = 1
                        self.map[i][j-1][self.DOOR_RIGHT] = 1
                    if seq[k] == self.DOOR_RIGHT:
                        #print("here3")
                        self.map[i][j][self.DOOR_RIGHT] = 1
                        self.map[i][j+1][self.DOOR_LEFT] = 1
                    return;

    def check_all_available(self,available_map):
        for i in range(self.row):
            for j in range(self.col):
                if available_map[i][j] == 0:
                    return False
        return True

    def clear_right(self, i, j):
        if i == self.row - 1:
            self.map[i][j][self.DOOR_UP] = 1
            self.map[i-1][j][self.DOOR_DOWN] = 1
        if j == self.col - 1:
            self.map[i][j][self.DOOR_LEFT] = 1
            self.map[i][j-1][self.DOOR_RIGHT] = 1

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
            if(not self.check_close_door(i,j,3)):
                self.map[i][j][self.DOOR_UP] = self.random_status();
            else:
                self.map[i][j][self.DOOR_UP] = 1;

    def generate_down_door(self, i, j):
        if i == self.row - 1:
            self.map[i][j][self.DOOR_DOWN] = -1
        elif self.map[i+1][j][self.DOOR_UP] != 0:
            self.map[i][j][self.DOOR_DOWN] = self.map[i+1][j][self.DOOR_UP]
        else:
            if(not self.check_close_door(i,j,3)):
                self.map[i][j][self.DOOR_DOWN] = self.random_status();
            else:
                self.map[i][j][self.DOOR_DOWN] = 1;

    def generate_left_door(self, i, j):
        if j == 0:
            self.map[i][j][self.DOOR_LEFT] = -1
        elif self.map[i][j-1][self.DOOR_RIGHT] != 0:
            self.map[i][j][self.DOOR_LEFT] = self.map[i][j-1][self.DOOR_RIGHT]
        else:
            if(not self.check_close_door(i,j,3)):
                self.map[i][j][self.DOOR_LEFT] = self.random_status();
            else:
                self.map[i][j][self.DOOR_LEFT] = 1;

    def generate_right_door(self, i, j):
        if j == self.col - 1:
            self.map[i][j][self.DOOR_RIGHT] = -1
        elif self.map[i][j+1][self.DOOR_LEFT] != 0:
            self.map[i][j][self.DOOR_RIGHT] = self.map[i][j+1][self.DOOR_LEFT]
        else:
            if(not self.check_close_door(i,j,3)):
                self.map[i][j][self.DOOR_RIGHT] = self.random_status();
            else:
                self.map[i][j][self.DOOR_RIGHT] = 1;

    def print_map(self):
        #print(self.map)
        for i in range(0, self.row):
            str = ' '
            for j in range(0, self.col):
                if self.map[i][j][self.DOOR_UP] == -1:
                    str += '-  '
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
                    str += '-  '
                else:
                    str += '   '
            print(str)

    def random_status(self):
        if(randint(0, 1) == 0):
            return 1
        else:
            return -1

    def how_many_close_door(self,i,j):
        count = 0
        for x in range(4):
            if self.map[i][j][x] == 0:
                count += 1
        return count

    def check_close_door(self,i,j,num):
        count = self.how_many_close_door(i,j)
        if count == num:
            return True
        return False
