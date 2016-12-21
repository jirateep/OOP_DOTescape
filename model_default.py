import arcade

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class Texture:
    def __init__(self,filename, x, y):
        self.img = arcade.Sprite(filename,1)
        self.img.left = x
        self.img.bottom = y

    def draw(self):
        self.img.draw()

class TextureCenter:
    def __init__(self,filename,x,y):
        self.img = arcade.Sprite(filename,1)
        self.img.center_x = x
        self.img.center_y = y

    def draw(self):
        self.img.draw()
