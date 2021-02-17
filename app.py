import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.K_ESCAPE:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.draw.rect(self._display_surf, "black", (0, 0, self.weight, self.height))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()



if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()