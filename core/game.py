from core.scene import Scene
from core.input import InputManager
from core.ui import UIManager

import pygame as pg
import os

class Game:
    def __init__(self, title="Game", width=800, height=600, is_editor=False):
        pg.init()
        pg.font.init()

        if is_editor:
            os.environ["SDL_VIDEO_DRIVER"] = "dummy"
            self.screen = pg.Surface((width, height))
        else:
            self.screen = pg.display.set_mode((width, height))
            
        self.caption = pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = False
        self.fps = 60
        self.scene = Scene()
        self.input_manager = InputManager()
        self.debug_mode = False
        self.ui_manager = UIManager()
               
        
    def toggle_debug(self):
        self.debug_mode = not self.debug_mode

    def run(self):
        self.running = True
        while self.running:
            
            # Events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_F1:
                    self.toggle_debug()
            
            # Update
            self.input_manager.update(events)
            if self.scene:
                self.scene.update(events)
            self.ui_manager.update(events)
            
            # Render
            self.screen.fill((0, 0, 0))
            if self.scene:
                self.scene.render(self.screen, debug_mode=self.debug_mode)
            self.ui_manager.render(self.screen)
            pg.display.flip()
            
            # FPS
            self.clock.tick(self.fps)
    
    def set_scene(self, scene):
        self.scene = scene