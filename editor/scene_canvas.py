import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk

class SceneCanvas(tk.Canvas):
    def __init__(self, parent, pygame_game_instance, width=800, height=600):
        super().__init__(parent, width=width, height=height, bg="black")
        self.pack(fill=tk.BOTH, expand=True)

        self.game = pygame_game_instance  # instance de Game avec is_editor=True
        self.tk_image = None

        self.after(16, self.update_canvas)  # Boucle de rendu

    def update_canvas(self):
        self.delete("all")

        # Appelle le moteur pour mettre à jour et dessiner la scène sur surface
        if self.game.scene:
            self.game.scene.update([])      # Pas d'events
            self.game.scene.render(self.game.screen)  # Rend sur self.game.screen

            self.tk_image = self.pygame_surface_to_tk_image(self.game.screen)
            self.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.after(16, self.update_canvas)

    def pygame_surface_to_tk_image(self, surface):
        """Convertit une surface Pygame en image Tkinter proprement"""
        width, height = surface.get_size()
        data = pg.image.tostring(surface, "RGB")  # ← Conversion fiable
        image = Image.frombytes("RGB", (width, height), data)
        return ImageTk.PhotoImage(image)