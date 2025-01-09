from core.components.transform import Transform

class GameObject:
    def __init__(self, name, x=0, y=0, description=""):
        self.name = name
        self.description = description
        self.components = {}
        self.children = []
        
        # Ajoute un composant Transform par défaut
        self.transform = Transform()
        self.transform.parent = self
        self.transform.position = (x, y)
        self.add_component(self.transform)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"
    
    def add_component(self, component):
        component.parent = self
        if component.__class__.__name__ in self.components:
            raise ValueError(f"Component {component.__class__.__name__} already exists")
        self.components[component.__class__.__name__] = component
        
        
    def get_component(self, component_name):
        return self.components.get(component_name)
    
    
    def update(self):
        for component in self.components.values():
            component.update()
            
    def add_child(self, child):
        """Ajoute un enfant à ce GameObject."""
        if not isinstance(child, GameObject):
            raise ValueError("Child must be an instance of GameObject")
        
        if child.parent:
            child.parent.remove_child(child)
        
        child.parent = self
        child.get_component("Transform").parent = self
        self.children.append(child)
        
    def remove_child(self, child):
        """Retire un enfant de ce GameObject."""
        if child in self.children:
            child.parent = None
            child.get_component("Transform").parent = None
            self.children.remove(child)
            
    def on_collision_enter(self, other):
        """Appelé lorsqu'une collision est détectée."""
        #print("f{self.name} collided with {other.name}")
        pass
    
    def on_trigger_enter(self, other):
        """Appelé lorsqu'une collision est détectée."""
        #print("f{self.name} triggered with {other.name}")
        pass
            
    