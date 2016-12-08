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
        self.score = 0
        self.player = Player(self, 450, 300)
        self.map = Map(self)
        self.end_this_level = False
        self.level = 1
        self.load_enermy()

    def animate(self, delta):
        self.player.animate(delta)
        for i in range(len(self.now_enermy)):
            self.now_enermy[i].animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.update_player_up_down(key,"press")
        self.update_player_left_right(key,"press")
        self.update_shield(key)

    def on_key_release(self, key, key_modifiers):
        self.update_player_up_down(key,"unpress")
        self.update_player_left_right(key,"unpress")

    def update_shield(self, key):
        if key == arcade.key.Z:
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
