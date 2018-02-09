import pygame, random

class Platformer(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path, width=70, height=70):
        super().__init__()
        self.image = pygame.Surface([width, height]).convert()
        self.image.blit(pygame.image.load(img_path).convert(), (0, 0), (0, 0, width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def scroll(self,change):
        screen_info = pygame.display.Info()
        self.rect.top += change
        if self.rect.top > screen_info.current_h:
            self.rect.top = -50
            self.rect.left = random.randint(5, (screen_info.current_w-50)//10)*10
