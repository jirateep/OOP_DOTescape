import arcade
from model_default import Model
from model_map import Map

class Player(Model):

    def __init__(self, world, x, y):
        super().__init__(world,x,y,0)
        self.room_position_x = 0
        self.room_position_y = 0
        self.direction_up_down = 0;
        self.direction_left_right = 0;
        self.key_collected = 0
        self.count_to_next_level = 0
        self.max_count_to_next_level = 600

    def update_direction_up_down(self,direction):
        if direction == arcade.key.UP:
            self.direction_up_down = 1
        elif direction == arcade.key.DOWN:
            self.direction_up_down = -1
        else:
            self.direction_up_down = 0

    def update_direction_left_right(self,direction):
        if direction == arcade.key.RIGHT:
            self.direction_left_right = 1
        elif direction == arcade.key.LEFT:
            self.direction_left_right = -1
        else:
            self.direction_left_right = 0

    def animate(self, delta):
        self.move()
        self.go_to_next_room()
        self.collected_key()
        self.end_level()

    def end_level(self):
        self.check_end_level()
        self.prepare_to_next_level()

    def prepare_to_next_level(self):
        if self.world.end_this_level:
            if self.count_to_next_level < self.max_count_to_next_level:
                self.count_to_next_level += 1
            else:
                self.count_to_next_level = 0
                self.world.make_new_level()

    def check_end_level(self):
        if [self.room_position_x, self.room_position_y] == [self.world.map.gate_x, self.world.map.gate_y]:
            if self.key_collected == self.world.map.num_of_key:
                if ((self.x - 450)**2 + (self.y - 300)**2)**(1/2.0) < 50:
                    self.world.end_this_level = True


    def collected_key(self):
        for i in range(len(self.world.map.keys)):
            if [self.room_position_x, self.room_position_y] == self.world.map.keys[i]:
                if self.world.map.keys_status[i]:
                    if ((self.x - 450)**2 + (self.y - 300)**2)**(1/2.0) < 25:
                        self.key_collected += 1
                        self.world.map.keys_status[i] = False

    def go_to_next_room(self):
        if self.x == 45 and self.y <= 375 and self.y >= 225:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_LEFT] == 1:
                self.room_position_y -= 1
                self.x = 850
        if self.x == 855 and self.y <= 375 and self.y >= 225:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_RIGHT] == 1:
                self.room_position_y += 1
                self.x = 50
        if self.y == 555 and self.x <= 525 and self.x >= 375:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_UP] == 1:
                self.room_position_x -= 1
                self.y = 50
        if self.y == 45 and self.x <= 525 and self.x >= 375:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_DOWN] == 1:
                self.room_position_x += 1
                self.y = 550

    def move(self):
        self.move_up_down()
        self.move_left_right()
        self.stay_in_range()

    def move_up_down(self):
        self.y += 5*self.direction_up_down

    def move_left_right(self):
        self.x += 5*self.direction_left_right

    def stay_in_range(self):
        if self.x < 45:
            self.x = 45
        if self.y < 45:
            self.y = 45
        if self.y > 555:
            self.y = 555
        if self.x > 855:
            self.x = 855
