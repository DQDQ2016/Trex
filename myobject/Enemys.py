import pygame
from random import *
from myobject import PrupleThunder

import myobject.stageControl as st

# 小型敌机的显示过程，从出现到被中弹到被毁灭到变成灰
class SoldierEnemy1(pygame.sprite.Sprite):
    energy = 5

    def __init__(self, bg_size,x,y):
        pygame.sprite.Sprite.__init__(self)
        # 中型敌机的图片，满血和中弹的更换
        self.image = pygame.image.load("data/images/enemy/soldier/aster_紫苑.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/enemy/soldier/aster_紫苑_hit.png").convert_alpha()
        # 中型敌机受到攻击后加载中弹到被毁到变灰的图片

        mwidth, mheight = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (mwidth // 2, mheight // 2))
        self.image_hit = pygame.transform.smoothscale(self.image_hit, (mwidth // 2, mheight // 2))

        boom1=pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        boom2=pygame.image.load("data/images/orther/boom2.png").convert_alpha()
        boom3=pygame.image.load("data/images/orther/boom3.png").convert_alpha()
        boom4=pygame.image.load("data/images/orther/boom4.png").convert_alpha()

        boom = pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        mwidth, mheight = boom.get_size()

        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.transform.smoothscale(boom1,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom2,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom3,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom4,(mwidth // 2,mheight // 2)), \
            ])


        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.show = True

        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.rect.left=x
        self.rect.top=y
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = SoldierEnemy1.energy
        self.hit = False

    # 中型敌机的移动方式
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 中型敌机中弹后的重置方式
    def reset(self):
        print("SoldierEnemy1  reset")
        st.stage+=1
        self.active = False
        self.show = False


# 陨石1的显示过程，从出现到被中弹到被毁灭到变成灰
class StoneEnemy1(pygame.sprite.Sprite):
    energy = 80
    def __init__(self, bg_size,x,y):
        pygame.sprite.Sprite.__init__(self)
        # 中型敌机的图片，满血和中弹的更换
        self.image = pygame.image.load("data/images/orther/yunshi1.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/orther/yunshi1_hit.png").convert_alpha()
        # 中型敌机受到攻击后加载中弹到被毁到变灰的图片

        mwidth, mheight = self.image.get_size()
        # self.image = pygame.transform.smoothscale(self.image, (mwidth // 2, mheight // 2))
        # self.image_hit = pygame.transform.smoothscale(self.image_hit, (mwidth // 2, mheight // 2))

        boom1=pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        boom2=pygame.image.load("data/images/orther/boom2.png").convert_alpha()
        boom3=pygame.image.load("data/images/orther/boom3.png").convert_alpha()
        boom4=pygame.image.load("data/images/orther/boom4.png").convert_alpha()

        boom = pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        # mwidth, mheight = boom.get_size()

        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.transform.smoothscale(boom1,(mwidth ,mheight )), \
            pygame.transform.smoothscale(boom2,(mwidth ,mheight )), \
            pygame.transform.smoothscale(boom3,(mwidth,mheight )), \
            pygame.transform.smoothscale(boom4,(mwidth ,mheight )), \
            ])


        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.show = True


        self.rect.left=x
        self.rect.top=y
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = StoneEnemy1.energy
        self.hit = False

    # 中型敌机的移动方式
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 中型敌机中弹后的重置方式
    def reset(self):
        print("StoneEnemy1  reset")
        st.stage+=1
        self.active = False
        self.show = False


# 陨石2的显示过程，从出现到被中弹到被毁灭到变成灰
class StoneEnemy2(pygame.sprite.Sprite):
    energy = 150

    def __init__(self, bg_size,x,y):
        pygame.sprite.Sprite.__init__(self)
        # 中型敌机的图片，满血和中弹的更换
        self.image = pygame.image.load("data/images/orther/yunshi2.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/orther/yunshi2_hit.png").convert_alpha()
        # 中型敌机受到攻击后加载中弹到被毁到变灰的图片

        mwidth, mheight = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (mwidth // 2, mheight // 2))
        self.image_hit = pygame.transform.smoothscale(self.image_hit, (mwidth // 2, mheight // 2))

        boom1=pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        boom2=pygame.image.load("data/images/orther/boom2.png").convert_alpha()
        boom3=pygame.image.load("data/images/orther/boom3.png").convert_alpha()
        boom4=pygame.image.load("data/images/orther/boom4.png").convert_alpha()

        boom = pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        # mwidth, mheight = boom.get_size()

        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.transform.smoothscale(boom1,(mwidth//2,mheight // 2 )), \
            pygame.transform.smoothscale(boom2,(mwidth //2,mheight // 2 )), \
            pygame.transform.smoothscale(boom3,(mwidth//2,mheight //2 )), \
            pygame.transform.smoothscale(boom4,(mwidth //2 ,mheight //2 )), \
            ])


        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.show = True

        self.rect.left=x
        self.rect.top=y
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = StoneEnemy2.energy
        self.hit = False

    # 中型敌机的移动方式
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 中型敌机中弹后的重置方式
    def reset(self):
        st.stage+=1
        self.active = False
        self.show = False
        print("StoneEnemy2  reset")



# 小型敌机的显示过程，从出现到被中弹到被毁灭到变成灰
class SoldierEnemy2(pygame.sprite.Sprite):
    energy = 5

    def __init__(self, bg_size,x,y):
        pygame.sprite.Sprite.__init__(self)
        # 中型敌机的图片，满血和中弹的更换
        self.image = pygame.image.load("data/images/enemy/soldier/Rosa_蔷薇.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/enemy/soldier/Rosa_蔷薇_hit.png").convert_alpha()
        # 中型敌机受到攻击后加载中弹到被毁到变灰的图片

        mwidth, mheight = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (mwidth // 2, mheight // 2))
        self.image_hit = pygame.transform.smoothscale(self.image_hit, (mwidth // 2, mheight // 2))

        boom1=pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        boom2=pygame.image.load("data/images/orther/boom2.png").convert_alpha()
        boom3=pygame.image.load("data/images/orther/boom3.png").convert_alpha()
        boom4=pygame.image.load("data/images/orther/boom4.png").convert_alpha()

        boom = pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        mwidth, mheight = boom.get_size()

        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.transform.smoothscale(boom1,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom2,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom3,(mwidth // 2,mheight // 2)), \
            pygame.transform.smoothscale(boom4,(mwidth // 2,mheight // 2)), \
            ])


        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.show = True

        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.rect.left=x
        self.rect.top=y
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = SoldierEnemy1.energy
        self.hit = False
        self.forRight=True

    # 中型敌机的移动方式
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
            if self.forRight:
                if self.rect.left<450:
                    self.rect.left+=2
                else:
                    self.forRight=False
            else:
                if self.rect.left>50:
                    self.rect.left-=2
                else:
                    self.forRight=True
        else:
            self.reset()

    # 中型敌机中弹后的重置方式
    def reset(self):
        st.stage+=1
        self.active = False
        print("SoldierEnemy2  reset")

        self.show = False




# BOSS的显示过程，从出现到被中弹到被毁灭到变成灰
class BossEnemy(pygame.sprite.Sprite):
    energy = 1000
    power = 100
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 中型敌机的图片，满血和中弹的更换
        self.image = pygame.image.load("data/images/enemy/boss/Dahlia_大丽花.png").convert_alpha()
        self.image_hit = pygame.image.load("data/images/enemy/boss/Dahlia_大丽花_hit.png").convert_alpha()
        # 中型敌机受到攻击后加载中弹到被毁到变灰的图片

        mwidth, mheight = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (mwidth, mheight))
        self.image_hit = pygame.transform.smoothscale(self.image_hit, (mwidth , mheight ))

        boom1=pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        boom2=pygame.image.load("data/images/orther/boom2.png").convert_alpha()
        boom3=pygame.image.load("data/images/orther/boom3.png").convert_alpha()
        boom4=pygame.image.load("data/images/orther/boom4.png").convert_alpha()

        # boom = pygame.image.load("data/images/orther/boom1.png").convert_alpha()
        # mwidth, mheight = boom.get_size()

        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.transform.smoothscale(boom1,(mwidth ,mheight)), \
            pygame.transform.smoothscale(boom2,(mwidth ,mheight)), \
            pygame.transform.smoothscale(boom3,(mwidth ,mheight)), \
            pygame.transform.smoothscale(boom4,(mwidth,mheight)), \
            ])


        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = False
        self.show = True
        self.shottype=0
        # self.rect.left, self.rect.top = \
        #     randint(0, self.width - self.rect.width), \
        #     randint(-10 * self.height, -self.height)
        self.rect.left=40
        self.rect.top=-300
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = BossEnemy.energy
        self.hit = False
        self.forRight=True

    # 中型敌机的移动方式
    def move(self):
        if self.rect.top<30:
            self.rect.top+=self.speed
        if self.forRight:
         if self.rect.left < 90:
             self.rect.left+=self.speed
         else:
             self.forRight=False
        else:
            if self.rect.left>10:
                self.rect.left-=self.speed
            else:
                self.forRight=True


    # 中型敌机中弹后的重置方式
    def reset(self):
        st.stage+=1
        print("boss reset")
        self.active = False
        self.show = False


