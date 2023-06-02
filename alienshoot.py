import pygame
 
class Alien_Shoot:
    def __init__(self, ai_game):
        pygame.init()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/ship2.0.bmp')
        self.screen_rect = ai_game.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.move_up = False
        self.move_down = False
 
    def update_position(self):
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 1
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
 
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)