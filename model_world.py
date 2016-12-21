import arcade
import arcade.key
from random import randint
from model_player import Player
from model_map import Map
from model_enermy import Enermy
from model_default import ModelSprite
class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.player = Player(self, 450, 300)
        self.map = Map(self)
        self.end_this_level = False
        self.load_enermy()
        self.show_required_end_task = False
        self.room_width = 900
        self.room_height = 600
        self.pause_status = False
        self.show_map_status = False

    def animate(self, delta):
        if not self.pause_status:
            self.player.animate(delta)
            for i in range(len(self.now_enermy)):
                self.now_enermy[i].animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.update_player_up_down(key,"press")
        self.update_player_left_right(key,"press")
        self.update_shield(key)
        self.update_pause_status(key)
        self.update_show_map_status(key)

    def on_key_release(self, key, key_modifiers):
        self.update_player_up_down(key,"unpress")
        self.update_player_left_right(key,"unpress")

    def update_pause_status(self, key):
        if key == arcade.key.P:
            print("pause")
            if self.pause_status:
                self.pause_status = False
            else:
                self.pause_status = True

    def update_show_map_status(self, key):
        if key == arcade.key.M:
            print("show map")
            if not pause_status:
                if self.show_map_status:
                    self.show_map_status = False
                    self.pause_status = False
                else:
                    self.show_map_status = True
                    self.pause_status = True

    def update_shield(self, key):
        if key == arcade.key.SPACE:
            self.player.shield = True

    def update_player_up_down(self, key, press_status):
        if key == arcade.key.UP:
            if press_status == "press":
                self.player.update_direction_up_down(arcade.key.UP)
            if press_status == "unpress":
                self.player.update_direction_up_down("STAY")
        elif key == arcade.key.DOWN:
            if press_status == "press":
                self.player.update_direction_up_down(arcade.key.DOWN)
            if press_status == "unpress":
                self.player.update_direction_up_down("STAY")

    def update_player_left_right(self, key, press_status):
        if key == arcade.key.LEFT:
            if press_status == "press":
                self.player.update_direction_left_right(arcade.key.LEFT)
            if press_status == "unpress":
                self.player.update_direction_left_right("STAY")
        elif key == arcade.key.RIGHT:
            if press_status == "press":
                self.player.update_direction_left_right(arcade.key.RIGHT)
            if press_status == "unpress":
                self.player.update_direction_left_right("STAY")

    def make_new_level(self):
        self.level += 1
        self.end_this_level = False
        if self.level % 2 == 0:
            self.map.row += 1
        else:
            self.map.col += 1
        self.map.make_new_map()
        self.player.key_collected = 0

    def load_enermy(self):
        self.now_enermy = []
        self.now_enermy_sprite = []
        if self.map.enermy[self.player.room_position_x][self.player.room_position_y] != 0:
            for i in range(self.map.enermy[self.player.room_position_x][self.player.room_position_y][Enermy.BLUE]):
                self.now_enermy.append(Enermy(self,Enermy.BLUE))
            for i in range(self.map.enermy[self.player.room_position_x][self.player.room_position_y][Enermy.GREEN]):
                self.now_enermy.append(Enermy(self,Enermy.GREEN))
            for i in range(len(self.now_enermy)):
                if self.now_enermy[i].speed == 1:
                    self.now_enermy_sprite.append(ModelSprite('images/blue_enermy.png',model=self.now_enermy[i]))
                else:
                    self.now_enermy_sprite.append(ModelSprite('images/green_enermy.png',model=self.now_enermy[i]))
