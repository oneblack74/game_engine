class InputManager:
    def __init__(self):
        self.actions = {}

    def create_action(self, name):
        action = InputAction(name)
        self.actions[name] = action
        return action

    def get_action(self, name):
        return self.actions.get(name)

    def update(self, events):
        for action in self.actions.values():
            action.update(events)
