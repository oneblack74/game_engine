from .ui_element import UIElement

import pygame as pg

class UIText(UIElement):
    def __init__(self, position, text, font_size=24, color=(255, 255, 255)):
        self.text = text
        self.font_size = font_size
        self.font = pg.font.Font(None, font_size)
        self.color = color
        self.surface = self.font.render(self.text, True, self.color)
        self.size = self.surface.get_size()
        super().__init__(position, self.size)
        
    def render(self, screen):
        if self.visible:
            screen.blit(self.surface, self.position)
            
    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.size = self.surface.get_size()