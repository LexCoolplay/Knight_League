import pygame
class GameObject(pygame.sprite.Sprite):
    def __init__(self,source,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=source
        self.rect=self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))