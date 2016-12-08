import arcade
from model_default import Model
from random import randint

class Enermy(Model):
    BLUE = 0
    GREEN = 1

    def __init__(self, world, green_or_blue):
        x = randint(150, 750)
        y = randint(150, 450)
        super().__init__(world, x, y, 0)
        if green_or_blue == self.BLUE:
            self.speed = 1
        else:
            self.speed = 2

    def animate(self, delta):
        self.move()
        self.move_scope()

    def move_scope(self):
        if self.x < 45:
            self.x = 45
        if self.y < 45:
            self.y = 45
        if self.y > 555:
            self.y = 555
        if self.x > 855:
            self.x = 855

    def move(self):
        if self.x > self.world.player.x:
            self.x -= self.speed
        else:
            self.x += self.speed
        if self.y > self.world.player.y:
            self.y -= self.speed
        else:
            self.y += self.speed
