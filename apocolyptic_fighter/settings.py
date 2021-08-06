import pygame, sys
pygame.init()

class settings(object):
    def __init__(self):
        # Display settings
        self.WIDTH, self.HEIGHT = (800, 800)
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Apocolyptic fighter')
        self.FPS = 30

        #Colors
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        #Background
        self.BACKGROUND = pygame.image.load('apocolyptic_fighter/Assets/Background.png')
        self.WIN.blit(self.BACKGROUND, (0, 0))