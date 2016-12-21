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
        self.pause_sprite = Texture('images/pauseBg.png',0,0)

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
        self.player_sprite.draw()
        for i in range(len(self.world.now_enermy_sprite)):
            self.world.now_enermy_sprite[i].draw()
        if self.world.pause_status:
            self.pause_sprite.draw()
        self.show_status()
        if self.world.show_map_status:
            self.show_map()
        self.left_status()

    def show_status(self):
        if self.world.pause_status and not self.world.show_map_status:
            arcade.draw_text("PAUSE", 450, 300, arcade.color.WHITE, 70, width=200, align="center", anchor_x="center", anchor_y="center")
        if self.world.end_this_level:
            arcade.draw_text("END LEVEL "+str(self.world.level), 300, 200, arcade.color.BLACK, 50)
        if self.world.player.is_dead:
            arcade.draw_text("YOU DIED\nREACH "+str(self.world.level - 1)+" LEVELS", 200, 300, arcade.color.BLACK, 50)
        if self.world.show_required_end_task:
            arcade.draw_text("NEED 2 KEYS TO OPEN", 150, 100, arcade.color.BLACK, 50)

    def show_map(self):
        self.draw_track()
        self.draw_room()

    def draw_track(self):
        center_x = self.room_sprite.img.center_x
        center_y = self.room_sprite.img.center_y
        col = self.world.map.col
        row = self.world.map.row
        for i in range(0, row):
            for j in range(0, col):
                if self.world.map.visited[i][j]:
                    for k in range(0, 4):
                        if self.world.map.map[i][j][k] == 1:
                            show_track_sprite = TextureCenter('images/track.png',self.cal_x_show_track(center_x,col,j,k),self.cal_y_show_track(center_y,row,i,k))
                            show_track_sprite.draw()

    def cal_x_show_track(self,center,max,now,door):
        x = self.cal_x_show_map(center,max,now)
        size = 50
        width = 5
        size_width = size + width
        if door == self.world.map.DOOR_LEFT:
            x -= (size_width)/2
        if door == self.world.map.DOOR_RIGHT:
            x += (size_width)/2
        return x

    def cal_y_show_track(self,center,max,now,door):
        y = self.cal_y_show_map(center,max,now)
        size = 50
        width = 5
        size_width = size + width
        if door == self.world.map.DOOR_DOWN:
            y -= (size_width)/2
        if door == self.world.map.DOOR_UP:
            y += (size_width)/2
        return y

    def draw_room(self):
        center_x = self.room_sprite.img.center_x
        center_y = self.room_sprite.img.center_y
        col = self.world.map.col
        row = self.world.map.row
        for i in range(0, row):
            for j in range(0, col):
                show_map_sprite = TextureCenter('images/' + self.set_img_show_map(i,j),self.cal_x_show_map(center_x,col,j),self.cal_y_show_map(center_y,row,i))
                show_map_sprite.draw()

    def set_img_show_map(self,x,y):
        if not self.world.map.visited[x][y]:
            return 'room_hide.png'
        elif [x,y] == [self.world.player.room_position_x,self.world.player.room_position_y]:
            return 'room_me.png'
        elif [x,y] == [self.world.map.gate_x,self.world.map.gate_y]:
            return 'room_gate.png'
        elif [x,y] in self.world.map.keys:
            show_key = False
            for i in range(0,len(self.world.map.keys)):
                if [x,y] == self.world.map.keys[i]:
                    if self.world.map.keys_status[i]:
                        return 'room_key.png'
            return 'room_free.png'
        else:
            return 'room_free.png'

    def cal_x_show_map(self,center,max,now):
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

    def cal_y_show_map(self,center,max,now):
        width = 5
        size = 50
        width_size = width + size
        mid = max / 2
        range = now - mid
        if max % 2 == 0:
            if now < mid:
                return center + width_size / 2 - (range + 1) * width_size
            else:
                return center - width_size / 2 - range * width_size
        else:
            return center - range * width_size

    def left_status(self):
        arcade.draw_text("LV.", 910, 570, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.level), 910, 520, arcade.color.WHITE, 35)
        arcade.draw_text("KEYS", 910, 200, arcade.color.WHITE, 25)
        arcade.draw_text(str(self.world.player.key_collected), 910, 150, arcade.color.WHITE, 35)
        #arcade.draw_text("COL", 910, 370, arcade.color.WHITE, 25)
        #arcade.draw_text(str(self.world.map.col), 910, 320, arcade.color.WHITE, 35)
        #arcade.draw_text("NOW ROW", 910, 300, arcade.color.WHITE, 12)
        #arcade.draw_text(str(self.world.player.room_position_x + 1), 910, 250, arcade.color.WHITE, 35)
        #arcade.draw_text("NOW COL", 910, 200, arcade.color.WHITE, 12)
        #arcade.draw_text(str(self.world.player.room_position_y + 1), 910, 150, arcade.color.WHITE, 35)
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
