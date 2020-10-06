import pygame


class TextDisplay(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pass
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("data/images/orther/context.png").convert_alpha()

        width, height = self.image1.get_size()
        self.image1 = pygame.transform.smoothscale(self.image1, (width+80, height))

        self.rect = self.image1.get_rect()
        backwidth, backheight = self.image1 .get_size()
        self.rect.top = bg_size[1]-backheight-10
        self.rect.left = 10

class ShowTitle1(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("data/images/orther/showtitle1.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.left=0
        self.rect.top=0

class ShowTitle2(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("data/images/orther/showtitle2.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.left=0
        self.rect.top=0



