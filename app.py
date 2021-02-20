import pygame
from intro import intro
from game import Game


class App:


    def __init__(self):
        self._running = True
        self.size = self.width, self.height = 640, 400
        self._display_surf = pygame.display.set_mode(self.size)
        self.intro_state = intro(self._display_surf, 640, 400)
        self.game_state = Game(self._display_surf, 640, 400)

    def on_init(self):
        pygame.init()

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.K_ESCAPE:
            self._running = False

    def state_manager(self):
        if self.intro_state.state == "intro":
            self.intro_state.main()
        if self.intro_state.state == "playing":
            self.game_state.main()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.state_manager()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()