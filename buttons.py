import pygame
pygame.init()
# button
class button(object):
    def __init__(self, msg, x, y, t_width, width, height, color, h_color, action):
        self.msg = msg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.h_color = h_color
        self.action = action
        self.font_small = pygame.font.SysFont("comicsans", t_width )
        self.text_msg = self.font_small.render(self.msg, 1, (0, 0, 0))

    def draw(self, win):
        # button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(win, self.h_color, ( self.x, self.y, self.width, self.height))
            win.blit(self.text_msg, (self.x + 1, self.y + 3))
            if click[0] == 1:
                self.action
  
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
            win.blit(self.text_msg, (self.x + 1, self.y + 3))
    
        
