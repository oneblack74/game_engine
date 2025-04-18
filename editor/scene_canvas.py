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

        if self.game.scene:
            self.game.update_for_editor()

            surface = self.game.screen

            game_width, game_height = surface.get_size()
            canvas_width = self.winfo_width()
            canvas_height = self.winfo_height()

            scale = min(canvas_width / game_width, canvas_height / game_height)
            new_width = int(game_width * scale)
            new_height = int(game_height * scale)
            offset_x = (canvas_width - new_width) // 2
            offset_y = (canvas_height - new_height) // 2

            pg_surface_rgb = pg.transform.scale(surface, (new_width, new_height))
            data = pg.image.tostring(pg_surface_rgb, "RGB")
            image = Image.frombytes("RGB", (new_width, new_height), data)

            self.tk_image = ImageTk.PhotoImage(image)
            self.create_image(offset_x, offset_y, anchor=tk.NW, image=self.tk_image)

        self.after(16, self.update_canvas)
