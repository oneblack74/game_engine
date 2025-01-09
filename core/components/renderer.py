from core.component import Component

import pygame as pg

class Renderer(Component):
    def __init__(self, color=(255, 255, 255), size=(50, 50)):
        super().__init__("Renderer")
        self.color = color
        self.size = size

    def draw(self, surface, position):
        pg.draw.rect(
            surface,
            self.color,
            pg.Rect(position[0], position[1], self.size[0], self.size[1])
        )

        