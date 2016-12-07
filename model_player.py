import arcade
from model_default import Model
from model_map import Map

class Player(Model):
    room_position_x = 0
    room_position_y = 0
    direction_up_down = 0;
    direction_left_right = 0;

    def __init__(self, world, x, y):
        super().__init__(world,x,y,0)

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
        self.goToNextRoom()

    def goToNextRoom(self):
        if self.x == 45 and self.y <= 375 and self.y >= 225:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_LEFT] == 1:
                self.room_position_y -= 1
        if self.x == 855 and self.y <= 375 and self.y >= 225:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_RIGHT] == 1:
                self.room_position_y += 1
        if self.y == 555 and self.x <= 555 and self.x >= 375:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_UP] == 1:
                self.room_position_x -= 1
        if self.y == 45 and self.x <= 555 and self.x >= 375:
            if self.world.map.map[self.room_position_x][self.room_position_y][Map.DOOR_DOWN] == 1:
                self.room_position_x += 1

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
