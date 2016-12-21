import arcade
import arcade.key
from model_default import ModelSprite, Texture, TextureCenter
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
        self.doors_sprite = [Texture('images/door_up.png',375,575),Texture('images/door_down.png',375,0),Texture('images/door_left.png',0,225),Texture('images/door_right.png',875,225)]
        self.player_sprite = ModelSprite('images/player.png',model=self.world.player)
        self.key_sprite = TextureCenter('images/key.png',self.room_sprite.img.center_x,self.room_sprite.img.center_y)
        self.gate_sprite = TextureCenter('images/gate.png',self.room_sprite.img.center_x,self.room_sprite.img.center_y)
        self.show_map_sprite = TextureCenter('images/map.png',self.room_sprite.img.center_x,self.room_sprite.img.center_y)

    def on_draw(self):
        arcade.start_render()
        self.room_sprite.draw()
        for i in range(len(self.doors_sprite)):
            if self.world.map.map[self.world.player.room_position_x][self.world.player.room_position_y][i] == 1:
                self.doors_sprite[i].draw()
        for i in range(len(self.world.map.keys)):
            if [self.world.player.room_position_x,self.world.player.room_position_y] == self.world.map.keys[i]:
                if self.world.map.keys_status[i]:
                    self.key_sprite.draw()
        if self.world.map.gate_x == self.world.player.room_position_x and self.world.map.gate_y == self.world.player.room_position_y:
            self.gate_sprite.draw()
        #arcade.draw_text(str(self.world.score), self.world.width - 30, self.world.height - 30, arcade.color.WHITE, 20)
        self.player_sprite.draw()
        for i in range(len(self.world.now_enermy_sprite)):
            self.world.now_enermy_sprite[i].draw()
        if self.world.pause_status and not self.world.show_map_status:
            arcade.draw_text("PAUSE", 300, 200, arcade.color.BLACK, 50)
        if self.world.end_this_level:
            arcade.draw_text("END LEVEL "+str(self.world.level), 300, 200, arcade.color.BLACK, 50)
        if self.world.player.is_dead:
            arcade.draw_text("YOU DIED\nREACH "+str(self.world.level - 1)+" LEVELS", 200, 300, arcade.color.BLACK, 50)
        if self.world.show_required_end_task:
            arcade.draw_text("NEED 2 KEYS TO OPEN", 150, 100, arcade.color.BLACK, 50)
        if self.world.show_map_status:
            self.show_map()
        self.left_status()

    def show_map(self):
        center_x = self.room_sprite.img.center_x
        center_y = self.room_sprite.img.center_y
        col = self.world.map.col
        row = self.world.map.row
        for i in range(0, row):
            for j in range(0, col):
                self.show_map_sprite.img.center_x = self.cal_x_y_show_map(center_x,col,j)
                self.show_map_sprite.img.center_y = self.cal_x_y_show_map(center_y,row,i)
                self.show_map_sprite.draw()

    def cal_x_y_show_map(self,center,max,now):
        width = 5
        size = 50
        width_size = width + size
        mid = max / 2
        range = now - mid
        if max % 2 == 0:
            if now < mid:
                return center - width_size / 2 + (range + 1) * width_size
            else:
                return center + width_size / 2 + range * width_size
        else:
            return center + range * width_size

    def left_status(self):
        arcade.draw_text("LV.", 910, 570, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.level), 910, 520, arcade.color.WHITE, 35)
        arcade.draw_text("ROW", 910, 470, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.map.row), 910, 420, arcade.color.WHITE, 35)
        arcade.draw_text("COL", 910, 370, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.map.col), 910, 320, arcade.color.WHITE, 35)
        arcade.draw_text("NOW ROW", 910, 300, arcade.color.WHITE, 12)
        arcade.draw_text(str(self.world.player.room_position_x + 1), 910, 250, arcade.color.WHITE, 35)
        arcade.draw_text("NOW COL", 910, 200, arcade.color.WHITE, 12)
        arcade.draw_text(str(self.world.player.room_position_y + 1), 910, 150, arcade.color.WHITE, 35)
        arcade.draw_text("BOMB", 910, 100, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.player.shield_count), 910, 50, arcade.color.WHITE, 35)

    def animate(self, delta):
        if not self.world.player.is_dead:
            self.world.animate(delta)
            self.player_sprite.set_position(self.world.player.x, self.world.player.y)
            for i in range(len(self.world.now_enermy_sprite)):
                self.world.now_enermy_sprite[i].set_position(self.world.now_enermy[i].x,self.world.now_enermy[i].y)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = DotEscapeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
