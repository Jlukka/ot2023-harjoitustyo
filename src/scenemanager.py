class SceneManager:
    def __init__(self):
        self.scenestack = []

    def enter_scene(self, scene):
        self.scenestack.append(scene)

    def exit_scene(self, scene):
        self.scenestack.pop()
