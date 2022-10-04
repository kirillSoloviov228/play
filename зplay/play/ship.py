import pygame
from pygame.sprite import  Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # Сoхранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)
        self.centerr = float(self.rect.centery)


        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    # Обновляет позиции корабля с учетом флага.
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.centerr += self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.top > 0:
            self.centerr -= self.ai_settings.ship_speed_factor
        
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center
        self.rect.centery = self.centerr

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.center = self.screen_rect.centerx
