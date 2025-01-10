from .ui_element import UIElement

import pygame as pg

class UIButton(UIElement):
    def __init__(self, position, size, text="", font_size=24, color=(200, 200, 200), hover_color=(150, 150, 150)):
        super().__init__(position, size, color)
        self.hover_color = hover_color
        self.default_color = color
        self.font = pg.font.Font(None, font_size)
        self.text = text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.call_back = None
        
    def render(self, screen):
        if self.visible:
            self.surface.fill(self.color)
            text_pos = (
                self.size[0] // 2 - self.text_surface.get_width() // 2,
                self.size[1] // 2 - self.text_surface.get_height() // 2,
            )
            self.surface.blit(self.text_surface, text_pos)
            screen.blit(self.surface, self.position)
            
    def set_call_back(self, call_back):
        self.call_back = call_back
        
    def update(self, events):
        mouse_pos = pg.mouse.get_pos()
        rect = pg.Rect(self.position, self.size)
        
        if rect.collidepoint(mouse_pos):
            self.color = self.hover_color
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if self.call_back:
                        self.call_back()
        else:
            self.color = self.default_color