class InputAction:
    def __init__(self, name):
        self.name = name
        self.keys = []
        self.state = {"pressed": False, "held": False, "released": False}

    def bind_key(self, key):
        if isinstance(key, tuple):
            self.keys.extend(key)
        else:
            self.keys.append(key)

    def update(self, events):
        self.state = {"pressed": False, "held": False, "released": False}
        for event in events:
            if event.type == pygame.KEYDOWN and event.key in self.keys:
                self.state["pressed"] = True
                self.state["held"] = True
            elif event.type == pygame.KEYUP and event.key in self.keys:
                self.state["released"] = True
                self.state["held"] = False

    def is_pressed(self):
        return self.state["pressed"]

    def is_held(self):
        return self.state["held"]

    def is_released(self):
        return self.state["released"]
