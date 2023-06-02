import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.bullet_speed = 1
        self.bullet_width = 8
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.screen = ai_game.screen
        self.rect = pygame.Rect(0, 0, self.bullet_width,self.bullet_height)
        self.rect.midright = ai_game.alienshoot.rect.midright
        self.x = float(self.rect.x)
 
    def update(self):
        self.x += self.bullet_speed
        self.rect.x = self.x
 
 
    def draw_bullets(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
 