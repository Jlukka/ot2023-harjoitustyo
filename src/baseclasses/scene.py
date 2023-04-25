class Scene:
    def __init__(self, scenemanager, is_overlay=False):
        self._scenemanager = scenemanager
        self.overlay = is_overlay

    def update(self, actions):
        pass

    def render(self, display):
        pass
