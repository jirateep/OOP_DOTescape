import arcade
import arcade.key
from random import randint
from model_player import Player
from model_map import Map

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.player = Player(self, 100, 100)
        self.map = Map()

    def animate(self, delta):
        self.player.animate(delta);

    def on_key_press(self, key, key_modifiers):
        self.update_player_up_down(key,"press")
        self.update_player_left_right(key,"press")

    def on_key_release(self, key, key_modifiers):
        self.update_player_up_down(key,"unpress")
        self.update_player_left_right(key,"unpress")

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