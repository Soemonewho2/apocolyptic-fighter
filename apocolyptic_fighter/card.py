import pygame, sys
pygame.init()
pygame.font.init()

class Cards(object):
    def __init__(self, rect, display):
        self.rect = rect
        self.isHovering = False
        self.display = display
        print(self.rect)

    def draw(self):
        pygame.draw.rect(self.display, (255, 255, 255), self.rect)

    def hover(self):
        self.pos = pygame.mouse.get_pos()
        if self.isHovering == False:
            if self.pos[0] in range(self.rect.x, self.rect.x + self.rect.width):
                if self.pos[1] in range(self.rect.y, self.rect.y + self.rect.width):
                    self.rect.y -= 250
                    self.isHovering = True
                    
        if self.isHovering == True:
            self.rect = pygame.draw.rect(self.display, (0, 200, 50), self.rect)
            if self.pos[0] not in range(self.rect.x, self.rect.x + self.rect.width):
                if self.pos[1] not in range(self.rect.y, self.rect.y + self.rect.width):
                    self.rect.y += 250
                    self.isHovering = False      
