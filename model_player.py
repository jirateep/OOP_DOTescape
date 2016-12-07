import arcade
from model_default import Model

class Player(Model):
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
    direction_up_down = 0;
    direction_left_right = 0;

    def __init__(self, world, x, y):
        super().__init__(world,x,y,0)
        self.direction = Player.DIR_VERTICAL

    def update_direction_up_down(self,direction):
        if direction == arcade.key.UP:
            self.direction_up_down = 1
        elif direction == arcade.key.DOWN:
            self.direction_up_down = -1
        else:
            self.direction_up_down = 0
        print (self.direction_up_down)

    def update_direction_left_right(self,direction):
        if direction == arcade.key.RIGHT:
            self.direction_left_right = 1
        elif direction == arcade.key.LEFT:
            self.direction_left_right = -1
        else:
            self.direction_left_right = 0

    def animate(self, delta):
        self.move()

    def move(self):
        self.move_up_down()
        self.move_left_right()

    def move_up_down(self):
        self.y += 5*self.direction_up_down

    def move_left_right(self):
        self.x += 5*self.direction_left_right
