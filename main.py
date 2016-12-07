import arcade
import arcade.key
from model_default import ModelSprite, Texture
from model_world import World
from model_player import Player

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class DotEscapeGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)
        self.room_sprite = Texture('images/room.png',0,0)
        self.doors = [Texture('images/door_up.png',375,575),Texture('images/door_down.png',375,0),Texture('images/door_left.png',0,225),Texture('images/door_right.png',875,225)]
        self.player_sprite = ModelSprite('images/player.png',model=self.world.player)

    def on_draw(self):
        arcade.start_render()
        self.room_sprite.draw()
        self.player_sprite.draw()
        for i in range(len(self.doors)):
            if self.world.map.map[self.world.player.roomPositionX][self.world.player.roomPositionY][i] == 1:
                self.doors[i].draw()
        #self.gold_sprite.draw()
        #arcade.draw_text(str(self.world.score), self.world.width - 30, self.world.height - 30, arcade.color.WHITE, 20)

    def animate(self, delta):
        self.world.animate(delta)
        self.player_sprite.set_position(self.world.player.x, self.world.player.y)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = DotEscapeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
