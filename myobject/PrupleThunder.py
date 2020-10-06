import pygame

# 我方飞机的类
class PrupleThunder(pygame.sprite.Sprite):
    # 我方飞机出现到中弹到被毁到变灰的过程
    energy = 10
    fight_on=False
    power=100
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 飞机火焰的动态效果
        self.image1 = pygame.image.load("data/images/trex/purple_thunder_2.png").convert_alpha()
        self.image2 = pygame.image.load("data/images/trex/purple_thunder_1.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/trex/purple_thunder_hit.png").convert_alpha()


        # 我方飞机出现到中弹到被毁到变灰的图片更换过程
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("data/images/orther/boom1.png").convert_alpha(), \
            pygame.image.load("data/images/orther/boom2.png").convert_alpha(), \
            pygame.image.load("data/images/orther/boom3.png").convert_alpha(), \
            pygame.image.load("data/images/orther/boom4.png").convert_alpha() \
            ])
        # 飞机被毁后重置（需要有生命数）
        width, height = self.image1.get_size()
        self.image1 = pygame.transform.smoothscale(self.image1, (width // 3, height // 3))
        self.image2 = pygame.transform.smoothscale(self.image2, (width // 3, height // 3))
        self.image_hit = pygame.transform.smoothscale(self.image_hit, (width // 3, height // 3))

        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 5
        self.active = True
        self.shottype=0
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)
        self.hit = False



    # 向上移动
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    # 向下移动
    def moveDown(self):
        if self.rect.bottom < self.height :
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height

    # 向左移动
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    # 向右移动
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    # 飞机被毁后重置（需要有生命数）
    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True