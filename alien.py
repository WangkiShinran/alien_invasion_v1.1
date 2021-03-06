import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image_ori = pygame.image.load('images/alien_by_R.png')
        self.image = self.image_ori # pygame.transform.scale(self.image_ori, [60, 58])
        self.settings = ai_game.settings
        self.rect = self.image_ori.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x