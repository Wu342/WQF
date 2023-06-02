import pygame

import unittest
from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class Test(unittest.TestCase):
    """测试所有类"""
    def test_alien(self):
        """测试Alien类"""
        ai=Settings()
        screen=pygame.display.set_mode((ai.screen_width, ai.screen_height))
        alien=Alien(ai,screen)
        self.assertTrue(alien)
        
    def test_bullet(self):
        """测试Bullet类"""
        ai=Settings()
        screen=pygame.display.set_mode((ai.screen_width, ai.screen_height))
        ship=Ship(ai, screen)
        bullet=Bullet(ai,screen,ship)
        self.assertTrue(bullet)
    
    def test_game_stats(self):
        """测试GameStatus类"""
        ai=Settings()
        game_stats=GameStats(ai)
        self.assertTrue(game_stats)
        
    def test_settings(self):
        """Settings"""
        settings=Settings()
        self.assertTrue(settings)
    
    def test_ship(self):
        """测试Ship类"""
        ai=Settings()
        screen=pygame.display.set_mode((ai.screen_width, ai.screen_height))
        ship=Ship(ai,screen)
        self.assertTrue(ship)
    
if __name__=='__main__':
    unittest.main()
