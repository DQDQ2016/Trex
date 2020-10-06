import pygame

# 默认的子弹
class TrexBeam(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/beam1.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width // 3, height // 3))
        self.rect = self.image.get_rect()

        left=position[0]
        left=left-4
        top=position[1]
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < -40:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = True

# Trex光束炮
class TrexBigBeam(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/bigbeam.png").convert_alpha()
        self.image2 = pygame.image.load("data/images/shot/bigbeam2.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width // 2, 800))
        self.image2 = pygame.transform.smoothscale(self.image2, (width // 2, 800))

        self.rect = self.image.get_rect()

        left=position[0]
        left=left-38
        top=-720+position[1]
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 12
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    # # 飞机移动，子弹需要跟延迟跟随飞机
    # def move(self):
    #     self.rect.top -= self.speed
    #     if self.rect.top < -40:
    #         self.active = False
    # # 飞机重置，子弹需要跟随飞机重置
    # def reset(self, position):
    #     left = position[0]
    #     left = left - 4
    #     top = position[1]
    #     self.rect.left = left
    #     self.rect.top = top
    #     self.active = True
# BOSS光束炮
class BossBigBeam(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/boss_big_beam.png").convert_alpha()
        self.image2 = pygame.image.load("data/images/shot/boss_big_beam2.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (50, 800))
        self.image2 = pygame.transform.smoothscale(self.image2, (50, 800))

        self.rect = self.image.get_rect()

        left=position[0]
        left=left-25
        top=position[1]+120
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 12
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    # # 飞机移动，子弹需要跟延迟跟随飞机
    # def move(self):
    #     self.rect.top -= self.speed
    #     if self.rect.top < -40:
    #         self.active = False
    # # 飞机重置，子弹需要跟随飞机重置
    # def reset(self, position):
    #     left = position[0]
    #     left = left - 4
    #     top = position[1]
    #     self.rect.left = left
    #     self.rect.top = top
    #     self.active = True
# 默认的子弹
class Soldier1Beam(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/beam2.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width // 3, height // 3))
        self.rect = self.image.get_rect()

        left=position[0]
        left=left-10
        top=position[1]
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):
        self.rect.top =  self.rect.top+self.speed
        if self.rect.top > 740:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = False

# BOSS的子弹2
class Soldier2BeamBoss(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/shot2.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (70 , 70 ))
        self.rect = self.image.get_rect()

        left=position[0]
        left=left-40
        top=position[1]+140
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):
        self.rect.top =  self.rect.top+self.speed
        if self.rect.top > 740:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = False


# BOSS的子弹1
class Soldier1BeamBoss(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/beam2.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width // 3, height // 3))
        self.rect = self.image.get_rect()

        left=x
        top=y
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):
        self.rect.top =  self.rect.top+self.speed
        if self.rect.top > 740:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = False


# 默认的子弹
class Soldier2Beam(pygame.sprite.Sprite):
    def __init__(self, position,target):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/shot1.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width // 3, height // 3))
        self.rect = self.image.get_rect()

        self.target=target

        self.toleft=False
        self.toright=False


        left=position[0]
        left=left-10
        top=position[1]
        self.rect.left=left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

        if self.target[0]>left:
            self.toright=True
        elif self.target[0]<left:
            self.toleft=True



    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):

        self.rect.top =  self.rect.top+self.speed
        if self.toleft:
            self.rect.left-=2
        elif self.toright:
            self.rect.left+=2

        print(self.toright)
        print(self.toleft)

        if self.rect.top > 740:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = False


# 默认的子弹
class boss2beam(pygame.sprite.Sprite):
    def __init__(self, position,target):
        pygame.sprite.Sprite.__init__(self)
        # 加载默认子弹的图像
        self.image = pygame.image.load("data/images/shot/shot3.png").convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (70 , 70 ))



        self.rect = self.image.get_rect()

        self.target = target

        self.toleft = False
        self.toright = False

        left = position[0]
        left = left - 10
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        print(self.rect.left)
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

        if self.target[0] > left:
            self.toright = True
        elif self.target[0] < left:
            self.toleft = True



    # 飞机移动，子弹需要跟延迟跟随飞机
    def move(self):

        self.rect.top =  self.rect.top+self.speed
        if self.toleft:
            self.rect.left-=2
        elif self.toright:
            self.rect.left+=2

        print(self.toright)
        print(self.toleft)

        if self.rect.top > 740:
            self.active = False
    # 飞机重置，子弹需要跟随飞机重置
    def reset(self, position):
        left = position[0]
        left = left - 4
        top = position[1]
        self.rect.left = left
        self.rect.top = top
        self.active = False