import pygame
import settings as set
import card as ca
pygame.init()

settings = set.settings()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                set.sys.exit()
        
        set.settings()
        pygame.display.update()


if __name__ == "__main__":
    main()