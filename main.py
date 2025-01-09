from core import *

def main():
    game = Game()
    
    # Crée une scène
    scene = Scene()

    # Ajoute un joueur
    player = GameObject("Player")
    player.add_component(Renderer(color=(0, 255, 0)))
    player.get_component("Transform").position = (400, 300)
    player.add_component(Move(name="Move", speed=1, input_manager=game.input_manager))
    
    scene.add_game_object(player)

    # Ajoute une caméra comme enfant du joueur
    camera = CameraObject(viewport_size=(800, 600))
    camera.get_component("Transform").position = (0, 0)  
    camera.get_component("Transform").parent = player
    scene.set_camera(camera)

    # Ajoute un objet statique
    static_object = GameObject("Static Object")
    static_object.add_component(Renderer(color=(255, 0, 0)))
    static_object.get_component("Transform").position = (600, 400)
    scene.add_game_object(static_object)
    
    game.set_scene(scene)
    
    game.run()
    
    
if __name__ == "__main__":
    main()