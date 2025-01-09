class Component:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def update(self):
        pass
    