import pygame


def main():
    pygame.init()

    # Game Config
    WIDTH = 400
    HEIGHT = 800
    FPS = 1
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    color = (255, 255, 255)

    def draw():
        screen.fill(color)
        pygame.display.flip()



    def collision():
        pass

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        draw()


if __name__ == '__main__':
    main()
