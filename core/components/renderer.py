from core.component import Component

import pygame as pg

class Renderer(Component):
    def __init__(self, parent, color=(255, 255, 255), size=(1, 1)):
        super().__init__("Renderer", parent=parent)
        self.color = color
        self.size = (size[0] * 50, size[1] * 50)
        
        if self.parent.get_component("SpriteRenderer"):
            raise Exception("GameObject already has a SpriteRenderer component")

    def draw(self, surface, position):
        pg.draw.rect(
            surface,
            self.color,
            pg.Rect(position[0], position[1], self.size[0], self.size[1])
        )

        