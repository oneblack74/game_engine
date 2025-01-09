from core.scene import Scene
from core.input import InputManager

import pygame as pg

class Game:
    def __init__(self, title="Game", width=800, height=600):
        self.screen = pg.display.set_mode((width, height))
        self.caption = pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = False
        self.fps = 60
        self.scene = Scene()
        self.input_manager = InputManager()
        self.debug_mode = False
               
        
    def toggle_debug(self):
        self.debug_mode = not self.debug_mode

    def run(self):
        self.running = True
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_F1:
                    self.toggle_debug()
            
            self.input_manager.update(events)
            self.scene.update(events)
            
            self.screen.fill((0, 0, 0))
            self.scene.render(self.screen, debug_mode=self.debug_mode)
            pg.display.flip()
            self.clock.tick(self.fps)
    
    def set_scene(self, scene):
        self.scene = scene