# main.py
# 导入包
import pygame
import sys



import traceback


# 文件来自pygame模块和random模块
from pygame.locals import *
from random import *

from myobject import PrupleThunder
from myobject import Textdisplay
from myobject import ShotBeam
from myobject import Enemys
from myobject import stageControl as st


pygame.init()
pygame.mixer.init()

# 设置宽高和标题名
bg_size = width, height = 490, 740
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Project_Trex")

background1 = pygame.image.load("data/images/orther/backstar.jpg").convert_alpha()
background2 = pygame.image.load("data/images/orther/backstar.jpg").convert_alpha()
background3 = pygame.image.load("data/images/orther/backstar.jpg").convert_alpha()
backwidth, backheight = background1.get_size()
background1 = pygame.transform.smoothscale(background1, (backwidth*2, backheight * 3))
background2 = pygame.transform.smoothscale(background1, (backwidth*2, backheight * 3))
background3 = pygame.transform.smoothscale(background1, (backwidth*2, backheight * 3))
backheight=backheight*3
# 载入游戏音乐

# 人物头像设置
iconbadman1 = pygame.image.load("data/images/icon/badman1.png").convert_alpha()
iconbadman2 = pygame.image.load("data/images/icon/badman2.png").convert_alpha()

iconboss = pygame.image.load("data/images/icon/boss.png").convert_alpha()
icontrex = pygame.image.load("data/images/icon/trex.jpg").convert_alpha()

iconboss = pygame.image.load("data/images/icon/boss.png").convert_alpha()
icontrex = pygame.image.load("data/images/icon/trex.jpg").convert_alpha()

shottitle1 = pygame.image.load("data/images/orther/showtitle1.png").convert_alpha()
shottitle2 = pygame.image.load("data/images/orther/showtitle2.png").convert_alpha()

# 设置颜色值（后续使用，先定义颜色值）
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
def pashe_1_music():
    pygame.mixer.music.load("data/song/James Shimoji - Yellow Line.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
def pashe_2_music():
    pygame.mixer.music.load("data/song/Daniel Sadowski - Crimson Assault.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
def pashe_3_music():
    pygame.mixer.music.load("data/song/Ki：Theory - KITTY HAWK.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
def pashe_4_music():
    pygame.mixer.music.load("data/song/James Shimoji - REDLINE.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
def them_music():
    pygame.mixer.music.load("data/song/戸田信子,陣内一真 - Bemular.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
# 增加小型敌机1
def add_small_enemies1_stage11(group1, group2):
        e1 = Enemys.SoldierEnemy1(bg_size,150,-50)
        e2 = Enemys.SoldierEnemy1(bg_size,300,-50)
        group1.add(e1)
        group2.add(e1)
        group1.add(e2)
        group2.add(e2)

# 增加小型敌机1
def add_small_enemies1_stage12(group1, group2):
        e1 = Enemys.SoldierEnemy1(bg_size,70,-100)
        e2 = Enemys.SoldierEnemy1(bg_size,170,-50)
        e3 = Enemys.SoldierEnemy1(bg_size,270,-50)
        e4= Enemys.SoldierEnemy1(bg_size,370,-100)
        group1.add(e1)
        group2.add(e1)
        group1.add(e2)
        group2.add(e2)
        group1.add(e3)
        group2.add(e3)
        group1.add(e4)
        group2.add(e4)

# 增加小型敌机1
def add_small_enemies1_stage17(group1, group2):
        e1 = Enemys.SoldierEnemy1(bg_size,100,-100)
        e2 = Enemys.SoldierEnemy1(bg_size,200,-200)
        e3 = Enemys.SoldierEnemy1(bg_size,300,-300)
        e4= Enemys.SoldierEnemy1(bg_size,400,-400)
        group1.add(e1)
        group2.add(e1)
        group1.add(e2)
        group2.add(e2)
        group1.add(e3)
        group2.add(e3)
        group1.add(e4)
        group2.add(e4)

# 增加小型敌机2
def add_small_enemies2_stage21(group1, group2):
        e1 = Enemys.SoldierEnemy2(bg_size,340,-100)
        e2 = Enemys.SoldierEnemy2(bg_size,240,-200)
        e3 = Enemys.SoldierEnemy2(bg_size,140,-300)
        e4= Enemys.SoldierEnemy2(bg_size,40,-400)
        group1.add(e1)
        group2.add(e1)
        group1.add(e2)
        group2.add(e2)
        group1.add(e3)
        group2.add(e3)
        group1.add(e4)
        group2.add(e4)


# 增加小型敌机2
def add_small_enemies2_stage25(group1, group2):
        e1 = Enemys.SoldierEnemy2(bg_size,40,-100)
        e2 = Enemys.SoldierEnemy2(bg_size,100,-200)
        e3 = Enemys.SoldierEnemy2(bg_size,330,-300)
        e4= Enemys.SoldierEnemy2(bg_size,200,-400)
        group1.add(e1)
        group2.add(e1)
        group1.add(e2)
        group2.add(e2)
        group1.add(e3)
        group2.add(e3)
        group1.add(e4)
        group2.add(e4)

# 增加小型敌机2
def add_small_enemies2_stage29(group_1,group_2, group2):
            e1 = Enemys.SoldierEnemy1(bg_size, 80, -200)
            e2 = Enemys.SoldierEnemy1(bg_size, 180, -100)
            e3 = Enemys.SoldierEnemy1(bg_size, 280, -100)
            e4 = Enemys.SoldierEnemy1(bg_size, 380, -200)
            e5 = Enemys.SoldierEnemy2(bg_size, 40, -100)
            e6 = Enemys.SoldierEnemy2(bg_size, 440, -100)
            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_1.add(e4)
            group2.add(e4)
            group_2.add(e5)
            group2.add(e5)
            group_2.add(e6)
            group2.add(e6)

# 增加小型敌机2
def add_small_enemies2_stage35(group_1,group_2, group2):
            e1 = Enemys.SoldierEnemy1(bg_size, 80, -100)
            e2 = Enemys.SoldierEnemy1(bg_size, 180, -200)
            e3 = Enemys.SoldierEnemy1(bg_size, 280, -300)
            e5 = Enemys.SoldierEnemy2(bg_size, 40, -100)
            e6 = Enemys.SoldierEnemy2(bg_size, 40, -200)
            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_2.add(e5)
            group2.add(e5)
            group_2.add(e6)
            group2.add(e6)

# 增加小型敌机2
def add_small_enemies2_stage76(group_1,group_2, group2):
            e1 = Enemys.SoldierEnemy1(bg_size, 40, -300)
            e2 = Enemys.SoldierEnemy1(bg_size, 140, -200)
            e3 = Enemys.SoldierEnemy1(bg_size, 240, -100)
            e5 = Enemys.SoldierEnemy1(bg_size, 340, -200)
            e6 = Enemys.SoldierEnemy1(bg_size, 440, -300)
            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_1.add(e5)
            group2.add(e5)
            group_1.add(e6)
            group2.add(e6)

# 增加小型敌机2
def add_small_enemies2_stage81(group_1,group_2, group2):
            e1 = Enemys.SoldierEnemy1(bg_size, 100, -100)
            e2 = Enemys.SoldierEnemy1(bg_size, 200, -100)
            e3 = Enemys.SoldierEnemy1(bg_size, 300, -100)
            e4 = Enemys.SoldierEnemy2(bg_size, 100, -200)
            e5 = Enemys.SoldierEnemy2(bg_size, 200, -200)
            e6 = Enemys.SoldierEnemy2(bg_size, 300, -200)
            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_2.add(e4)
            group2.add(e4)
            group_2.add(e5)
            group2.add(e5)
            group_2.add(e6)
            group2.add(e6)


# 增加小型敌机2
def add_small_enemies2_stage85(group_1,group_2,group_3, group2):
            e1 = Enemys.SoldierEnemy1(bg_size, 200, -230)
            e2 = Enemys.SoldierEnemy1(bg_size, 260, -230)

            e3 = Enemys.StoneEnemy1(bg_size, 20, -100)
            e4 = Enemys.StoneEnemy1(bg_size, 320, -100)

            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_3.add(e3)
            group2.add(e3)
            group_3.add(e4)
            group2.add(e4)

# 增加小型敌机2
def add_small_enemies2_stage90(group_1,group_2,group_3, group2):
            e1 = Enemys.SoldierEnemy2(bg_size, 100, -330)
            e2 = Enemys.SoldierEnemy2(bg_size, 360, -330)
            e3 = Enemys.StoneEnemy2(bg_size, 20, -200)

            e4 = Enemys.SoldierEnemy1(bg_size, 100, -430)
            e5 = Enemys.SoldierEnemy2(bg_size, 200, -530)
            e6 = Enemys.SoldierEnemy1(bg_size, 360, -430)
            e7 = Enemys.StoneEnemy1(bg_size, 350, -630)

            e8 = Enemys.StoneEnemy1(bg_size, 250, -900)
            e9 = Enemys.SoldierEnemy1(bg_size, 20, -950)
            e10 = Enemys.SoldierEnemy1(bg_size, 150, -950)
            e11 = Enemys.SoldierEnemy2(bg_size, 190, -1400)
            e12 = Enemys.SoldierEnemy2(bg_size, 260, -1400)
            e13 = Enemys.StoneEnemy1(bg_size, 20, -1200)


            group_1.add(e4)
            group2.add(e4)
            group_1.add(e5)
            group2.add(e5)
            group_1.add(e9)
            group2.add(e9)
            group_1.add(e10)
            group2.add(e10)

            group_2.add(e12)
            group2.add(e12)
            group_2.add(e11)
            group2.add(e11)
            group_2.add(e6)
            group2.add(e6)
            group_2.add(e1)
            group2.add(e1)
            group_2.add(e2)
            group2.add(e2)

            group_3.add(e3)
            group2.add(e3)
            group_3.add(e8)
            group2.add(e8)
            group_3.add(e7)
            group2.add(e7)
            group_3.add(e13)
            group2.add(e13)

# 增加陨石
def add_Stone_enemies2_stage46(group_1, group2):
            e1 = Enemys.StoneEnemy1(bg_size, 330, -200)
            e2 = Enemys.StoneEnemy2(bg_size, 10, -400)
            e3 = Enemys.StoneEnemy1(bg_size, 50, -700)
            e4 = Enemys.StoneEnemy1(bg_size, 300, -600)
            e5 = Enemys.StoneEnemy2(bg_size, 360, -1000)
            e6 = Enemys.StoneEnemy1(bg_size, 10, -1200)
            e7 = Enemys.StoneEnemy1(bg_size, 110, -950)

            e8 = Enemys.StoneEnemy2(bg_size, 10, -1700)
            e9 = Enemys.StoneEnemy2(bg_size, 100, -1500)
            e10 = Enemys.StoneEnemy1(bg_size, 210, -1300)

            e11 = Enemys.StoneEnemy1(bg_size, 300, -2000)
            e12 = Enemys.StoneEnemy2(bg_size, 200, -2340)
            e13 = Enemys.StoneEnemy1(bg_size, 30, -2100)

            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_1.add(e4)
            group2.add(e4)
            group_1.add(e5)
            group2.add(e5)
            group_1.add(e6)
            group2.add(e6)
            group_1.add(e7)
            group2.add(e7)
            group_1.add(e8)
            group2.add(e8)
            group_1.add(e9)
            group2.add(e9)
            group_1.add(e10)
            group2.add(e10)
            group_1.add(e11)
            group2.add(e11)
            group_1.add(e12)
            group2.add(e12)
            group_1.add(e13)
            group2.add(e13)



# 增加陨石
def add_Stone_enemies2_stage48(group_1, group2):
            e1 = Enemys.StoneEnemy1(bg_size, 330, -200)
            e2 = Enemys.StoneEnemy2(bg_size, 10, -400)
            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)

# 增加陨石
def add_Stone_enemies2_stage62(group_1, group2):
            e1 = Enemys.StoneEnemy1(bg_size, 10, -200)
            e2 = Enemys.StoneEnemy1(bg_size, 120, -200)
            e3 = Enemys.StoneEnemy1(bg_size, 300, -200)
            e4 = Enemys.StoneEnemy1(bg_size, 400, -200)


            e5 = Enemys.StoneEnemy1(bg_size, 10, -460)
            e6 = Enemys.StoneEnemy2(bg_size, 100, -800)
            e7 = Enemys.StoneEnemy1(bg_size, 340, -550)
            e8 = Enemys.StoneEnemy1(bg_size, 500, -750)



            e9 = Enemys.StoneEnemy1(bg_size, 10, -1200)
            e10 = Enemys.StoneEnemy1(bg_size, 120, -1200)
            e11 = Enemys.StoneEnemy1(bg_size, 300, -1200)
            e12 = Enemys.StoneEnemy1(bg_size, 400, -1200)

            group_1.add(e1)
            group2.add(e1)
            group_1.add(e2)
            group2.add(e2)
            group_1.add(e3)
            group2.add(e3)
            group_1.add(e4)
            group2.add(e4)

            group_1.add(e5)
            group2.add(e5)
            group_1.add(e6)
            group2.add(e6)
            group_1.add(e7)
            group2.add(e7)
            group_1.add(e8)
            group2.add(e8)

            group_1.add(e9)
            group2.add(e9)
            group_1.add(e10)
            group2.add(e10)
            group_1.add(e11)
            group2.add(e11)
            group_1.add(e12)
            group2.add(e12)


# 小型敌机1射击
def add_small_enemies1_shot(group1, group2):
        e1 = Enemys.SoldierEnemy1(bg_size,100,30)
        group1.add(e1)


def showhp(hp):
    font = pygame.font.SysFont("SimHei", 24)
    mtext = font.render("HP:"+str(hp*10)+"%", True, WHITE)
    screen.blit(mtext, (10, 20))
def showloser(mtext):
    screen.blit(mtext, (50, 200))

def showpower(pw):
    font = pygame.font.SysFont("SimHei", 24)
    mtext = font.render("limit:"+str(pw)+"%", True, WHITE)
    screen.blit(mtext, (370, 20))

def showtext(micon, name, mtext,textback):

    font=pygame.font.SysFont("SimHei", 18)
    mtext=font.render(mtext,True,WHITE)
    name=font.render(name,True,WHITE)
    screen.blit(textback.image1, textback.rect)

    if micon!=0:
        micon = pygame.transform.smoothscale(micon, (60, 60))
        screen.blit(micon, (30,575))

    screen.blit(mtext, (40, 650))
    screen.blit(name, (100, 615))



def main():
    them_music()
    bullet_sound = pygame.mixer.Sound("data/sound/bullet.wav")
    bullet_sound.set_volume(0.1)
    boom_sound = pygame.mixer.Sound("data/sound/boom3.wav")
    boom_sound.set_volume(0.3)
    shot_boom_sound = pygame.mixer.Sound("data/sound/hit.wav")
    shot_boom_sound.set_volume(0.2)
    shot_beam_sound_1 = pygame.mixer.Sound("data/sound/beam.wav")
    shot_beam_sound_1.set_volume(0.2)
    #boss_射击定时
    BOSS_shot = USEREVENT
    BOSS_shot2 = USEREVENT+1

    font = pygame.font.SysFont("SimHei", 44)
    mtext = font.render("失败,退出重新开始。", True, RED)

    # 敌人加载
    enemies = pygame.sprite.Group()

    # 生成敌方小型飞机
    small_enemies1 = pygame.sprite.Group()
    small_enemies2 = pygame.sprite.Group()

    #生成敌方陨石
    stone_enemies = pygame.sprite.Group()

    #生成敌方boss
    boss_enemies = pygame.sprite.Group()

    beloser = False

    # 生成我方飞机
    text = Textdisplay.TextDisplay(bg_size)
    title1=Textdisplay.ShowTitle1(bg_size)
    title2=Textdisplay.ShowTitle2(bg_size)
    trex = PrupleThunder.PrupleThunder(bg_size)

    # 用于切换图片
    switch_image = True

    #是否处于战斗状态
    # 用于延迟
    delay = 100

    running = True
    # trex机体启动
    trex.active=0

    #背景图片循环
    back1=0
    back2=0-backheight
    back3=0-backheight*2
    #背景图是否滚动
    backrun=0

    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    # BULLET1_NUM = 4
    # for i in range(BULLET1_NUM):
        # bullet1.append(ShotBeam.TrexBeam(trex.rect.midtop))

    # bullet_big=[]

    #敌人子弹
    enemybeam = []
    enemybeam_index = 0

    big_boss=Enemys.BossEnemy(bg_size)


    while running:
        print(st.stage)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标点击
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text.rect.collidepoint(event.pos):
                    if st.stage!=11 and st.stage != 62 and st.stage!=46 and st.stage!=107:
                        st.stage=st.stage+1
                    pass
                if event.button ==1 and beloser:
                    pygame.quit()
                    sys.exit()
                    beloser=False
                    if st.stage==110 or st.stage==108:
                        st.stage=102
                    else:
                        st.stage = 2

                    trex.fight_on=True
                    big_boss.energy=1000
                    big_boss.active=False
                    for e in small_enemies1:
                        e.active = False
                        enemies.remove(e)
                    for e in small_enemies2:
                        e.active = False
                        enemies.remove(e)
                    for e in stone_enemies:
                        e.active = False
                        enemies.remove(e)
                    for e in small_enemies1:
                        e.active = False
                        enemies.remove(e)
                    for e in enemies:
                        e.active=False
                        enemies.remove(e)
                    for e in enemybeam:
                        e.active=False
                        enemybeam.remove(e)
                    trex.energy=10
            elif event.type == MOUSEMOTION:
                pass
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if  trex.power == 100 and st.stage >= 62:
                        trex.shottype=1
                    pass
                pass
            elif event.type ==  BOSS_shot:
                if big_boss.active:
                   x=randint(0,400)
                   enemybeam.append(ShotBeam.boss2beam(big_boss.rect.midtop, trex.rect.midtop))
                   enemybeam.append(ShotBeam.boss2beam(big_boss.rect.midtop, (x,trex.rect.midtop[1])))
            elif event.type == BOSS_shot2:
                if big_boss.active and big_boss.shottype==0:
                    enemybeam.append(ShotBeam.Soldier2BeamBoss(big_boss.rect.midtop))
                pass

        #脚本敌人控制
        enemey_show=False
        enemey_show=False
        for each in enemies:
            if each.active:
                enemey_show=True




        screen.blit(background1, (0, back1))
        screen.blit(background2, (0, back2))
        screen.blit(background3, (0, back3))
        if backrun:
            back1 = back1 + 2
            back2 = back2 + 2
            back3 = back3 + 2
            if (back1 > height):
                back1 = 0 - backheight * 2
            if (back2 > height):
                back2 = 0 - backheight * 2
            if (back3 > height):
                back3 = 0 - backheight * 2

        # 检测用户的键盘操作（wasd，上下左右）
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            trex.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            trex.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            trex.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            trex.moveRight()





        if not enemey_show:
            if st.stage == 13:
                add_small_enemies1_stage12(small_enemies1, enemies)
            elif st.stage==17:
                add_small_enemies1_stage17(small_enemies1, enemies)
            elif st.stage==21:
                add_small_enemies2_stage21(small_enemies2, enemies)
            elif st.stage == 25:
                add_small_enemies2_stage25(small_enemies2, enemies)
            elif st.stage==29:
                trex.active = 1
                add_small_enemies2_stage29(small_enemies1,small_enemies2, enemies)
            elif st.stage == 46:
                add_Stone_enemies2_stage46(stone_enemies, enemies)
            elif st.stage == 62:
                add_Stone_enemies2_stage62(stone_enemies, enemies)
            elif st.stage==35:
                add_small_enemies2_stage35(small_enemies1,small_enemies2, enemies)
            elif st.stage==74:
                add_small_enemies2_stage76(small_enemies1,small_enemies2, enemies)
            elif st.stage==79:
                add_small_enemies2_stage81(small_enemies1,small_enemies2, enemies)
            elif st.stage == 85:
                add_small_enemies2_stage85(small_enemies1, small_enemies2,stone_enemies, enemies)
            elif st.stage == 89:
                add_small_enemies2_stage90(small_enemies1, small_enemies2,stone_enemies, enemies)

        if st.stage==0:
            screen.blit(title1.image1, title1.rect)
        if st.stage==1:
            screen.blit(title2.image1, title2.rect)
        if st.stage==3:
            showtext(iconbadman1,'宇宙海盗1',"反抗的人全都杀掉",text)
        elif st.stage==2:
            showtext(0,'',"宇宙历432年，月球附近某宇宙矿场   (点击继续)",text)
        elif st.stage==4:
            showtext(iconbadman2,'宇宙海盗2',"这片宙域的矿场是我们的了！哈哈哈",text)
        elif st.stage==5:
            showtext(icontrex,'???',"这可不一定",text)
        elif st.stage == 6:
            showtext(iconbadman2, '宇宙海盗1', "？！是谁", text)
        elif st.stage == 7:
            showtext(iconbadman2, '宇宙海盗2', "谁胆敢和我们弗加洛兄弟会作对！？", text)
        elif st.stage == 8:
            showtext(iconbadman2, '宇宙海盗2', "等等..这个机体，难道是！", text)
        elif st.stage == 9:
            showtext(iconbadman1, '宇宙海盗1', "管他是谁，干就完了！", text)
        elif st.stage == 10:
            trex.fight_on = True
            trex.active = 1
            pashe_1_music()
            backrun = 1
            add_small_enemies1_stage11(small_enemies1, enemies)
            print("start")
            st.stage = 11
        elif st.stage == 40:
            trex.energy=10
            trex.active=False
            trex.fight_on = False
            them_music()
            showtext(iconbadman2, '宇宙海盗2', "没错！就是他！ 这个机体是USS的「紫色雷电」！", text)
        elif st.stage == 41:
            showtext(iconbadman2, '宇宙海盗2', "而他的驾驶员，就是那个臭名昭著的........", text)
        elif st.stage == 42:
            showtext(icontrex, 'TRex', "没错就是我，今天碰到我算你们倒霉了。", text)
        elif st.stage == 43:
            showtext(iconbadman1, '宇宙海盗1', "这样下去死定了。。怎么办！", text)
        elif st.stage == 44:
            showtext(iconbadman2, '宇宙海盗2', "前面有一片废弃的矿场！我们从那逃！", text)
        elif st.stage == 45:
            showtext(iconbadman1, '宇宙海盗1', "哈哈！天无绝人之路，我们快逃出去和主力会合！", text)
            pashe_2_music()
        elif st.stage == 46:
            trex.active = 1
            trex.fight_on = True
        elif st.stage == 59:
            trex.energy=10
            trex.active=False
            trex.fight_on = False
            them_music()
            showtext(icontrex, 'TRex', "啧，真是麻烦。", text)
        elif st.stage == 60:
            showtext(icontrex, 'TRex', "就用光束炮吧。", text)
        elif st.stage == 61:
            showtext(0,'',"击中敌人积蓄能量，能量值满后按空格使用激光炮",text)
            pashe_4_music()
        elif st.stage == 62:
            trex.active = True
            trex.fight_on = True
            trex.energy = 10
        elif st.stage==102:
            trex.energy = 10
            trex.active = False
            trex.fight_on = False
            showtext(iconbadman1, '宇宙海盗1', "终于和主力部队会合了", text)
        elif st.stage==103:
            showtext(iconboss, '迪瓦兹', "嚯，原来是USS的走狗", text)
        elif st.stage==104:
            showtext(iconboss, '迪瓦兹', "就让我来对付你吧", text)
        elif st.stage==105:
            showtext(iconbadman2, '宇宙海盗2', "迪瓦兹大人出手了，这家伙死定了，哈啊哈哈！", text)
        elif st.stage==106:
            showtext(icontrex, 'TRex', "呵", text)
        elif st.stage==107:
            pashe_3_music()
            big_boss.active = True
            trex.active = 1
            enemies.add(big_boss)
            trex.fight_on = True
            pygame.time.set_timer(BOSS_shot, 3 * 1000)
            pygame.time.set_timer(BOSS_shot2, 5 * 1000)
            st.stage=108
        elif st.stage==130:
            trex.energy = 10
            trex.active = False
            trex.fight_on = False
            showtext(iconboss, '迪瓦兹', "怎么可能！！！！", text)
        elif st.stage==131:
            showtext(icontrex, 'TRex', "去死吧", text)
        elif st.stage==132:
            showtext(iconboss, '迪瓦兹', "唔啊啊啊啊啊啊", text)
        elif st.stage==133:
            showtext(iconbadman2, '宇宙海盗2', "居然连老大也被他打败了！", text)
        elif st.stage==134:
            showtext(iconbadman1, '宇宙海盗1', "快逃命吧", text)
        elif st.stage==135:
            showtext(icontrex, 'TRex', "给我滚出这片宙域", text)
        elif st.stage == 136:
            showtext(0,'',"紫电霸王龙的传说还在继续",text)
        elif st.stage == 137:
            showtext(0,'',"to be continued",text)
        elif st.stage ==138:
            pygame.quit()
            sys.exit()

        if trex.shottype==0:
         if not (delay % 10) and trex.fight_on:
             bullet_sound.play()
             bullet1.append(ShotBeam.TrexBeam(trex.rect.midtop))

        if not (delay % 99):
            for each in small_enemies1:
                if each.active:
                    # 敌人子弹
                    enemybeam.append(ShotBeam.Soldier1Beam(each.rect.midtop))
                    pass
            for each in small_enemies2:
                if each.active:
                    # 敌人子弹
                    enemybeam.append(ShotBeam.Soldier2Beam(each.rect.midtop,trex.rect.midtop))
                    pass
            if big_boss.active:
                    p=big_boss.rect.midtop
                    x=p[0]
                    y=p[1]+140
                    enemybeam.append(ShotBeam.Soldier1BeamBoss(x-100,y))
                    enemybeam.append(ShotBeam.Soldier1BeamBoss(x-120,y))
                    enemybeam.append(ShotBeam.Soldier1BeamBoss(x+100,y))
                    enemybeam.append(ShotBeam.Soldier1BeamBoss(x+120,y))
                    pass
            # bullet_sound.play()
            # if is_double_bullet:
            #     bullets = bullet2
            #     bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
            #     bullets[bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
            #     bullet2_index = (bullet2_index + 2) % BULLET2_NUM
            # else:
            #     bullets = bullet1
            #     bullets[bullet1_index].reset(me.rect.midtop)
            #     bullet1_index = (bullet1_index + 1) % BULLET1_NUM

        # 检测子弹是否击中敌机
        if trex.active and trex.fight_on:
            if trex.shottype == 0:
              for b in bullet1:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                if enemy_hit:
                    shot_boom_sound.play()
                    b.active = False
                    bullet1.remove(b)
                    for e in enemy_hit:
                          e.hit = True
                          e.energy -= 1
                          if trex.power < 100 and trex.shottype==0:
                              trex.power += 1
                          if e.energy == 0:
                             boom_sound.play()
                             e.active = False

              for b in bullet1:
                   if b.active == False:
                    bullet1.remove(b)
            elif trex.shottype==1:
                bullet_big = ShotBeam.TrexBigBeam(trex.rect.midtop)
                if switch_image:
                    screen.blit(bullet_big.image, bullet_big.rect)
                else:
                    screen.blit(bullet_big.image2, bullet_big.rect)
                enemy_hit = pygame.sprite.spritecollide(bullet_big, enemies, False, pygame.sprite.collide_mask)
                if enemy_hit:
                    shot_boom_sound.play()
                    for e in enemy_hit:
                        e.hit = True
                        e.energy -= 1
                        if e.energy == 0:
                            boom_sound.play()
                            e.active = False
                pass
        #soldier1 子弹
        for each in enemybeam:
            if  each.active:
                screen.blit(each.image, each.rect)
                each.move()
            pass

        # 绘制中型敌机1：
        for each in small_enemies1:
            if each.active:
                each.move()
                if each.hit:
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
                else:
                    screen.blit(each.image, each.rect)

            else:
                # 毁灭
                if not (delay % 3):
                    if each.show:
                         screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                         e2_destroy_index = (e2_destroy_index + 1) % 4
                         each.reset()

        # 绘制BOSS：

        if big_boss.active:
                if big_boss.shottype==1:
                  boss_big_shot = ShotBeam.BossBigBeam(big_boss.rect.midtop)
                  enemybeam.append(boss_big_shot)
                  if switch_image:
                    screen.blit(boss_big_shot.image, boss_big_shot.rect)
                  else:
                    screen.blit(boss_big_shot.image2, boss_big_shot.rect)

                if big_boss.energy==250 or big_boss.energy==500 or big_boss.energy==750:
                    big_boss.shottype=1
                    big_boss.power=100
                big_boss.move()
                if big_boss.hit:
                    screen.blit(big_boss.image_hit, big_boss.rect)
                    big_boss.hit = False
                else:
                    screen.blit(big_boss.image, big_boss.rect)

        else:
                # 毁灭
                if not (delay % 3):
                    if big_boss.show:
                         screen.blit(big_boss.destroy_images[e2_destroy_index], big_boss.rect)
                         e2_destroy_index = (e2_destroy_index + 1) % 4
                         if big_boss.energy<=0:
                             big_boss.reset()
                             st.stage=130

        # 绘制陨石
        for each in stone_enemies:
            if each.active:
                each.move()
                if each.hit:
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
                else:
                    screen.blit(each.image, each.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    if each.show:
                         screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                         e2_destroy_index = (e2_destroy_index + 1) % 4
                         each.reset()

        # 绘制中型敌机：
        for each in small_enemies2:
            if each.active:
                each.move()
                if each.hit:
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
                else:
                    screen.blit(each.image, each.rect)

            else:
                # 毁灭
                if not (delay % 3):
                    if each.show:
                         screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                         e2_destroy_index = (e2_destroy_index + 1) % 4
                         each.reset()

        # 检测我方飞机是否被撞
        enemies_down = pygame.sprite.spritecollide(trex, enemies, False, pygame.sprite.collide_mask)
        enemies_down_beam = pygame.sprite.spritecollide(trex, enemybeam, False, pygame.sprite.collide_mask)
        if  not trex.invincible:
            if  enemies_down_beam or enemies_down:
                cont=False
                for e in enemies_down:
                    if e.active==True:
                        cont=e.active
                        print("hit1")
                        break
                for e in enemies_down_beam:
                    if e.active==True:
                        cont=e.active
                        print("hit2")
                        enemybeam.remove(e)
                        break
                    if e.speed==12 and big_boss.shottype==1:
                        print("hit3")
                        cont=True
                        break
                if cont:
                    trex.hit = True

                for e in enemies_down:
                    # enemybeam.remove(e)
                    e.active = False

        if trex.active:
            showhp(trex.energy)
            if st.stage>=62:
                showpower(trex.power)
            if trex.hit:
                screen.blit(trex.image_hit, trex.rect)
                trex.energy-=1
                if trex.energy == 0:
                    trex.active = False
                    trex.fight_on=False
                    beloser=True

                trex.hit = False
            else:
               if switch_image:
                  screen.blit(trex.image1, trex.rect)
               else:
                  screen.blit(trex.image2, trex.rect)

                # 切换图片
        if not (delay % 10):
            switch_image = not switch_image

        if not (delay % 2 ):
            if trex.shottype == 1:
                trex.power -= 1
                if trex.power == 0:
                    trex.shottype = 0
            if big_boss.shottype==1:
                big_boss.power-=1
                if big_boss.power==0:
                    big_boss.shottype=0

        if not (delay % 99):
            if trex.shottype == 1:
                shot_beam_sound_1.play()
            for e in enemies:
                if not e.active:
                    enemies.remove(e)

        if beloser:
            showloser(mtext)
            them_music()

        delay -= 1
        if not delay:
            delay = 100
        pygame.display.flip()
        clock.tick(60)



main()
