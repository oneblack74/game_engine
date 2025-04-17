import tkinter as tk
import threading
import core
from editor.scene_canvas import SceneCanvas

class EditorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Engine Editor")
        self.geometry("1000x600")

        # === Crée une instance du moteur en mode éditeur ===
        self.game = core.Game(is_editor=True)
        self.scene = core.Scene()
        self.game.set_scene(self.scene)

        # === Ajoute des GameObjects dans la scène ===
        camera = core.CameraObject()
        self.scene.set_camera(camera)


        player = core.GameObject("Player", x=100, y=100)
        player.add_component(core.Renderer(player, color=(0, 255, 0)))
        self.scene.add_game_object(player)

        cube = core.GameObject("Cube", x=200, y=150)
        cube.add_component(core.Renderer(cube, color=(255, 0, 0)))
        self.scene.add_game_object(cube)

        # === Scène Canvas connecté au moteur ===
        self.scene_canvas = SceneCanvas(self, self.game)
        self.scene_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # === Panneau de contrôle à droite ===
        controls = tk.Frame(self)
        controls.pack(side=tk.RIGHT, fill=tk.Y)

        play_button = tk.Button(controls, text="Play", command=self.launch_game)
        play_button.pack(pady=10)

    def launch_game(self):
        threading.Thread(target=self.start_game, daemon=True).start()

    def start_game(self):
        # Lance le moteur en mode "jeu" (avec vraie fenêtre Pygame)
        game = core.Game(is_editor=False)
        game.set_scene(self.scene)
        game.run()
