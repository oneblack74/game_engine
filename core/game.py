from core.scene import Scene

import pygame as pg

class Game:
    def __init__(self, title="Game", width=800, height=600):
        self.screen = pg.display.set_mode((width, height))
        self.caption = pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = False
        self.fps = 60
        self.scene = Scene()

    def run(self):
        self.running = True
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
            
            self.scene.update(events)
            self.scene.render(self.screen)
            pg.display.flip()
            self.clock.tick(self.fps)
    
    def set_scene(self, scene):
        self.scene = scene