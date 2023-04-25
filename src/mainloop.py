import pygame


class MainLoop:
    def __init__(self, event_queue, clock, renderer):
        self._event_queue = event_queue
        self._clock = clock
        self._renderer = renderer

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
