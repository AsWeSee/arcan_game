import pygame
from pygame.locals import *




class Game(object):
    def main(self, screen):
        clock =pygame.time.Clock()

        image = pygame.image.load('player.png')
        image_x = 100
        image_y = 100
        mod = 1
        while 1:
            clock.tick(60) #slowing down to 30 times in second
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            if image_x >= 300:
                mod = -1
            elif image_x <= 100:
                mod = 1
            image_x += mod
            screen.fill((210,120,120))
            screen.blit(image, (image_x, image_y)) #block image transport
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 720))
    Game().main(screen)
