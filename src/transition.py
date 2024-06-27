from .settings import *


class Transition:
    def __init__(self, reset, finish_reset):

        # setup
        self.display_surface = pygame.display.get_surface()
        self.reset = reset
        self.finish_reset = finish_reset

        # overlay image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.color = 255
        self.speed = -2

    def play(self):
        self.color += self.speed
        if self.color <= 0:
            self.speed *= -1
            self.color = 0
            self.reset()
        if self.color > 255:
            self.color = 255
            self.speed = -2
            self.finish_reset()

        self.image.fill((self.color, self.color, self.color))
        self.display_surface.blit(self.image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
