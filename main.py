from core import *

def main():
    game = Game()
    
    # Crée une scène
    scene = Scene()

    # Ajoute un joueur
    player = GameObject("Player", x=400, y=300)
    player.add_component(Renderer(color=(0, 255, 0)))
    player.add_component(Move(speed=1, input_manager=game.input_manager))
    player.add_component(Collider(1, 1))
    
    scene.add_game_object(player)

    # Ajoute une caméra comme enfant du joueur
    camera = CameraObject(viewport_size=(800, 600))
    camera.get_component("Transform").parent = player
    scene.set_camera(camera)

    # Ajoute un objet statique
    static_object = GameObject("Static Object", x=600, y=400)
    static_object.add_component(Renderer(color=(255, 0, 0)))
    static_object.add_component(Collider(1, 1))
    scene.add_game_object(static_object)
    
    game.set_scene(scene)
    
    game.run()
    
    
if __name__ == "__main__":
    main()