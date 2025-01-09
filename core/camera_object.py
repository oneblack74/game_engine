from core.game_object import GameObject
from core.camera import Camera

class CameraObject(GameObject):
    def __init__(self, name="Camera", viewport_size=(800, 600)):
        super().__init__(name)
        self.add_component(Camera(viewport_size))
