from core.component import Component

import pygame as pg

class Collider(Component):
    def __init__(self, width, height, name="Collider", is_trigger=False):
        super().__init__(name=name)
        self.is_trigger = is_trigger
        self.width = width * 50
        self.height = height * 50
        self.bounds = (width, height)
        
    def check_collision(self, other):
        """
        Vérifie la collision avec un autre collider.
        """
        if isinstance(other, Collider):
            return self.get_bounds().colliderect(other.get_bounds())
        else:
            raise TypeError("Collision avec un type de collider non pris en charge")
        
        
    def get_bounds(self):
        """
        Renvoie les limites (position et taille) du collider.
        """
        position = self.parent.transform.position
        return pg.Rect(position[0], position[1], self.width, self.height)
    
    def resolve_collision(self, other):
        """
        Calcule et applique la résolution de collision.
        """
        if isinstance(other, Collider):
            bounds1 = self.get_bounds()
            bounds2 = other.get_bounds()
            
            # Valcul de la distance miniamle pour séparer les deux objets
            dx = min(bounds1.right - bounds2.left, bounds2.right - bounds1.left)
            dy = min(bounds1.bottom - bounds2.top, bounds2.bottom - bounds1.top)
            
            # On déplace l'objet le moins loin possible
            if abs(dx) < abs(dy):
                correction = (dx if bounds1.centerx > bounds2.centerx else -dx, 0)
            else:
                correction = (0, dy if bounds1.centery > bounds2.centery else -dy)
                
            # Applique la correction
            self.parent.transform.translate(correction[0], correction[1])