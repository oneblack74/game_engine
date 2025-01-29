from core.component import Component
import pygame as pg

class SpriteRenderer(Component):
    
    def __init__(self, sprite, parent, size=1):
        super().__init__("SpriteRenderer", parent=parent)
        self.sprite = sprite
        self.size = size
        self._resize_sprite()
        
        if self.parent.get_component("Renderer"):
            raise Exception("GameObject already has a Renderer component")
        
    def _resize_sprite(self):
        self.sprite = pg.transform.scale(self.sprite, (int(self.sprite.get_width() * self.size), int(self.sprite.get_height() * self.size)))

    def set_size(self, new_size):
        self.size = new_size
        self._resize_sprite()

    def draw(self, surface, position):
        surface.blit(self.sprite, position)