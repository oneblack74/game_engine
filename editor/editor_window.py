import tkinter as tk
import threading
import core
from editor.scene_canvas import SceneCanvas

class EditorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Engine Editor")
        self.geometry("1000x600")

        # Scène Canvas
        self.scene_canvas = SceneCanvas(self)
        self.scene_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Panneau de contrôle à droite
        controls = tk.Frame(self)
        controls.pack(side=tk.RIGHT, fill=tk.Y)

        play_button = tk.Button(controls, text="Play", command=self.launch_game)
        play_button.pack(pady=10)

        # Crée une scène et quelques objets
        self.game = core.Game()
        self.scene = core.Scene()
        self.scene_canvas.set_scene(self.scene)

        player = core.GameObject("Player")
        player.get_component("Transform").position = (100, 100)
        self.scene.add_game_object(player)

        cube = core.GameObject("Cube")
        cube.get_component("Transform").position = (200, 150)
        self.scene.add_game_object(cube)

    def launch_game(self):
        threading.Thread(target=self.start_game, daemon=True).start()

    def start_game(self):
        self.game.set_scene(self.scene)
        self.game.run()

if __name__ == "__main__":
    editor_window = EditorWindow()
    editor_window.mainloop()
