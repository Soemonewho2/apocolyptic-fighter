import pygame, sys
pygame.init()
pygame.font.init()

display = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('card test')
card = pygame.rect.Rect(20, 750, 200, 300)
card1 = pygame.rect.Rect(250, 750, 200, 300)
card2 = pygame.rect.Rect(480, 750, 200, 300)
card3 = pygame.rect.Rect(710, 750, 200, 300)
font = pygame.font.SysFont('comicsans', 20, bold=True)

class Cards(object):
    def __init__(self, rect, font):
        self.rect = rect
        self.isHovering = False
        print(self.rect)

    def draw(self):
        pygame.draw.rect(display, (255, 255, 255), self.rect)

    def hover(self):
        self.pos = pygame.mouse.get_pos()
        if self.isHovering == False:
            if self.pos[0] in range(self.rect.x, self.rect.x + self.rect.width):
                if self.pos[1] in range(self.rect.y, self.rect.y + self.rect.width):
                    self.rect.y -= 250
                    self.isHovering = True
                    
        if self.isHovering == True:
            self.rect = pygame.draw.rect(display, (0, 200, 50), self.rect)
            if self.pos[0] not in range(self.rect.x, self.rect.x + self.rect.width):
                if self.pos[1] not in range(self.rect.y, self.rect.y + self.rect.width):
                    self.rect.y += 250
                    self.isHovering = False
                
        
                

Card = Cards(rect=card, font=font)
Card1 = Cards(card1, font)
Card2 = Cards(card2, font)
Card3 = Cards(card3, font)

run = True
while True:
    display.fill((0,0,0))
    Card.draw()
    Card.hover()

    Card1.draw()
    Card1.hover()

    Card2.draw()
    Card2.hover()

    Card3.draw()
    Card3.hover()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
    pygame.display.update()
        
