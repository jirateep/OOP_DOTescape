import arcade
import arcade.key
from models import World, Player, ModelSprite

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class DotEscapeGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.player_sprite = ModelSprite('images/player.png',model=self.world.player)
        #self.gold_sprite = ModelSprite('images/gold.png',model=self.world.gold)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        #self.gold_sprite.draw()
        #arcade.draw_text(str(self.world.score), self.world.width - 30, self.world.height - 30, arcade.color.WHITE, 20)

    def animate(self, delta):
        self.world.animate(delta)
        self.player_sprite.set_position(self.world.player.x, self.world.player.y)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = DotEscapeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
