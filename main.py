from core import *
import pygame as pg
from editor import *

def main():
    game = Game()
    
    # Crée une scène
    scene = Scene()

    # Ajoute un joueur
    player = GameObject("Player", x=400, y=300)
    #player.add_component(Renderer(player, color=(0, 255, 0)))
    player.add_component(Move(speed=1, input_manager=game.input_manager))
    player.add_component(Collider(1, 1))
    
    sprite = pg.image.load("assets/images/player/0.png")
    player.add_component(SpriteRenderer(sprite, player, size=3))
    
    scene.add_game_object(player)

    # Ajoute une caméra comme enfant du joueur
    camera = CameraObject(viewport_size=(800, 600))
    camera.get_component("Transform").parent = player
    scene.set_camera(camera)

    # Ajoute un objet statique
    static_object = GameObject("Static Object", x=600, y=400)
    static_object.add_component(Renderer(static_object, color=(255, 0, 0)))
    static_object.add_component(Collider(1, 1))
    scene.add_game_object(static_object)
    
    # Ajoute un objet déclencheur
    trigger_object = GameObject("Trigger Object", x=200, y=200)
    trigger_object.add_component(Collider(1, 1, is_trigger=True))
    scene.add_game_object(trigger_object)
    
    game.set_scene(scene)
    
    # Créer un text
    text = UIText((100, 100), "Hello World!", font_size=50, color=(0, 0, 255))
    game.ui_manager.add_element(text)
    
    # Créer un bouton
    button = UIButton((0, 0), (200, 50), text="Click me")
    button.set_call_back(lambda: print("Button clicked"))
    game.ui_manager.add_element(button)
    
    
    game.run()
    
    
if __name__ == "__main__":
    #main()
    editor_window = EditorWindow()
    editor_window.mainloop()