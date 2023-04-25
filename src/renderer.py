import pygame


class Renderer:
    def __init__(self, display, scenemanager):
        self._display = display
        self.scenemanager = scenemanager
        self._scenestack = self.scenemanager.scenestack

    def render(self):
        # print(self._scenestack)
        first_real_scene = -1
        if len(self._scenestack) >= 1:
            i = -1
            while self._scenestack[i].overlay and len(self._scenestack) >= abs(i):
                i -= 1
                first_real_scene -= 1

        for i in range(first_real_scene, 0, 1):
            # print(f"r {i}")
            self._scenestack[i].render(self._display)

        pygame.display.update()
