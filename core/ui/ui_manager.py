class UIManager:
    def __init__(self):
        self.elements = []
    
    def add_element(self, element):
        self.elements.append(element)
        
    def render(self, screen):
        for element in self.elements:
            element.render(screen)
            
    def update(self, events):
        for element in self.elements:
            element.update(events)