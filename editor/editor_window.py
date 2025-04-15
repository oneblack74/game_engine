import tkinter as tk
import threading
import core

class EditorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Engine Editor")
        self.geometry("400x300")

        play_button = tk.Button(self, text="Play", command=self.launch_game)
        play_button.pack(pady=10)

    def launch_game(self):
        threading.Thread(target=self.start_game, daemon=True).start()

    def start_game(self):
        game = core.Game()
        
        # Crée une scène
        scene = core.Scene()

        camera = core.CameraObject(viewport_size=(800, 600))
        scene.set_camera(camera)

        game.set_scene(scene)

        game.run()

if __name__ == "__main__":
    editor_window = EditorWindow()
    editor_window.mainloop()
