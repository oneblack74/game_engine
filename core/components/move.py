from core.component import *

import pygame as pg

class Move(Component):
    def __init__(self,name, speed=1, input_manager=None):
        super().__init__(name=name)
        self.speed = speed
        self.input_manager = input_manager
        
        self.move_action_up = input_manager.create_action("move_up")
        self.move_action_right = input_manager.create_action("move_right")
        self.move_action_down = input_manager.create_action("move_down")
        self.move_action_left = input_manager.create_action("move_left")
        
        self.move_action_up.add_key_binding(pg.K_z)
        self.move_action_up.add_key_binding(pg.K_UP)
        
        self.move_action_right.add_key_binding(pg.K_d)
        self.move_action_right.add_key_binding(pg.K_RIGHT)
        
        self.move_action_down.add_key_binding(pg.K_s)
        self.move_action_down.add_key_binding(pg.K_DOWN)
        
        self.move_action_left.add_key_binding(pg.K_q)
        self.move_action_left.add_key_binding(pg.K_LEFT)
        
        
    def update(self):
        if self.input_manager:
            if self.move_action_up.is_held():
                self.parent.transform.translate(0, -self.speed)
            if self.move_action_right.is_held():
                self.parent.transform.translate(self.speed, 0)
            if self.move_action_down.is_held():
                self.parent.transform.translate(0, self.speed)
            if self.move_action_left.is_held():
                self.parent.transform.translate(-self.speed, 0)
                
        else:
            raise ValueError("Input manager is not set in Move component")