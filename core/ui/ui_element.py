import pygame as pg

class UIElement:
    def __init__(self, position, size, color=(255, 255, 255)):
        self.position = position
        self.size = size
        self.color = color
        self.surface = pg.Surface(size)
        self.visible = True
        
    def render(self, screen):
        if self.visible:
            self.surface.fill(self.color)
            screen.blit(self.surface, self.position)
            
    def update(self, events):
        pass