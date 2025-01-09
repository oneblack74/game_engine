from core.component import Component

class Transform(Component):
    def __init__(self, position=(0, 0), rotation=0, scale=(1, 1)):
        super().__init__("Transform")
        self.local_position = position
        self.local_rotation = rotation
        self.local_scale = scale
        self.parent = None
        
        
    @property
    def position(self):
        """Retourne la position globale calculée en fonction du parent."""
        if self.parent:
            parent_transform = self.parent.get_component("Transform")
            if parent_transform and parent_transform is not self:  # Éviter une boucle infinie
                parent_position = parent_transform.position
                return (
                    self.local_position[0] + parent_position[0],
                    self.local_position[1] + parent_position[1],
                )
        return self.local_position
    
    @position.setter
    def position(self, value):
        """Ajuste la position locale en fonction de la position globale."""
        if self.parent:
            parent_transform = self.parent.get_component("Transform")
            if parent_transform and parent_transform is not self:  # Éviter une boucle infinie
                parent_position = parent_transform.position
                self.local_position = (
                    value[0] - parent_position[0],
                    value[1] - parent_position[1],
                )
            else:
                self.local_position = value
        else:
            self.local_position = value
    
    @property
    def rotation(self):
        """Retourne la rotation globale calculée en fonction du parent."""
        if self.parent:
            parent_rotation = self.parent.get_component("Transform").rotation
            if parent_rotation:
                return self.local_rotation + parent_rotation
        return self.local_rotation
    
    @rotation.setter
    def rotation(self, value):
        """Ajuste la rotation locale en fonction de la rotation globale."""
        if self.parent:
            parent_rotation = self.parent.get_component("Transform").rotation
            if parent_rotation:
                self.local_rotation = value - parent_rotation
        else:
            self.local_rotation = value
            
    @property
    def scale(self):
        """Retourne l'échelle globale calculée en fonction du parent."""
        if self.parent:
            parent_scale = self.parent.get_component("Transform").scale
            if parent_scale:
                return (
                    self.local_scale[0] * parent_scale[0],
                    self.local_scale[1] * parent_scale[1],
                )
        return self.local_scale
    
    @scale.setter
    def scale(self, value):
        """Ajuste l'échelle locale en fonction de l'échelle globale."""
        if self.parent:
            parent_scale = self.parent.get_component("Transform").scale
            if parent_scale:
                self.local_scale = (
                    value[0] / parent_scale[0],
                    value[1] / parent_scale[1],
                )
        else:
            self.local_scale = value

    def translate(self, x, y):
        self.local_position = (
            self.local_position[0] + x,
            self.local_position[1] + y,
        )

    def rotate(self, angle):
        self.local_rotation += angle

        # Garde la rotation dans l'intervalle [0, 360]
        self.local_rotation %= 360


    def resize(self, scale_x, scale_y):
        self.local_scale = (scale_x, scale_y)

    def resize_uniform(self, scale):
        self.local_scale = (scale, scale)
