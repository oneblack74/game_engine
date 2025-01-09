from core.components.transform import Transform
from core.game_object import GameObject

class Camera:
    def __init__(self, viewport_size=(800, 600)):
        self.viewport_size = viewport_size  # Taille de la fenêtre
        self.parent = None  # Sera assigné via `add_component`

    def world_to_screen(self, world_position):
        """
        Convertit une position dans le monde en coordonnées d'écran
        en fonction de la position de la caméra.
        """
        if not self.parent:
            raise ValueError("Camera must be attached to a GameObject")
        
        camera_transform = self.parent.get_component("Transform")
        camera_pos = camera_transform.position

        # Déplace le point par rapport à la caméra
        return (
            world_position[0] - camera_pos[0] + self.viewport_size[0] // 2,
            world_position[1] - camera_pos[1] + self.viewport_size[1] // 2,
        )
