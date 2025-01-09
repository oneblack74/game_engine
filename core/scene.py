from core.game_object import GameObject
from core.camera_object import CameraObject

class Scene:
    def __init__(self):
        self.game_objects = []
        self.camera = None
        
    def add_game_object(self, game_object):
        self.game_objects.append(game_object)
        
    def set_camera(self, camera_object):
        if not isinstance(camera_object, CameraObject):
            raise ValueError("CameraObject must be an instance of CameraObject")
        
        if not camera_object.get_component("Camera"):
            raise ValueError("CameraObject must have a Camera component")
        
        self.camera = camera_object
        
    def update(self, events):
        #self.input_manager.update(events)
        for game_object in self.game_objects:
            game_object.update()
            
    def render(self, surface):
        if not self.camera:
            raise ValueError("No camera set for the scene")

        # Récupère la caméra et son Transform
        camera_component = self.camera.get_component("Camera")
        camera_transform = self.camera.get_component("Transform")

        for game_object in self.game_objects:
            renderer = game_object.get_component("Renderer")
            if renderer:
                transform = game_object.get_component("Transform")
                screen_position = camera_component.world_to_screen(transform.position)
                renderer.draw(surface, screen_position)
