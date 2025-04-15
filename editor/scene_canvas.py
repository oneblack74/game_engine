import tkinter as tk

class SceneCanvas(tk.Canvas):
    def __init__(self, parent, width=800, height=600):
        super().__init__(parent, width=width, height=height, bg="gray20")
        self.pack(fill=tk.BOTH, expand=True)

        self.scene = None
        self.selected_object = None

        self.bind("<Button-1>", self.on_click)
        self.after(16, self.update_canvas)  # 60 FPS

    def set_scene(self, scene):
        self.scene = scene

    def update_canvas(self):
        self.delete("all")

        if self.scene:
            for obj in self.scene.game_objects:
                transform = obj.get_component("Transform")
                if transform:
                    x, y = transform.position
                    size = 30

                    fill_color = "yellow" if obj == self.selected_object else "lightblue"
                    self.create_rectangle(x, y, x + size, y + size, fill=fill_color)
                    self.create_text(x + size // 2, y - 10, text=obj.name, fill="white")

        self.after(16, self.update_canvas)

    def on_click(self, event):
        if not self.scene:
            return

        for obj in self.scene.game_objects:
            transform = obj.get_component("Transform")
            if transform:
                x, y = transform.position
                size = 30
                if x <= event.x <= x + size and y <= event.y <= y + size:
                    self.selected_object = obj
                    print(f"Sélectionné : {obj.name}")
                    break