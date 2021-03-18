import pygame as pg
import random as r
import math
from os import *


# Attribution
####################################################################
#Code Anthony Garrard
#Art Work Credit "Kenney.nl" or "www.kenney.nl"

####################################################################

# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0

    def update(self):
       # print(self.rect)
        self.rect.x += self.speedx

        # keystate = pg.key.get_pressed()
        # if keystate[pg.K_SPACE]:
        #     self.shoot()
        # if keystate[pg.K_a] or keystate[pg.K_LEFT]:
        #     self.speedx = -5
        # if keystate[pg.K_d] or keystate[pg.K_RIGHT]:
        #     self.speedx = 5

        if self.rect.right >= WIDTH-1 or self.rect.left<=0:
            self.speedx = 0
        if self.rect.top <=0 or self.rect.bottom>=HEIGHT-1:
            self.speedy = 0

    def shoot(self):
        b = Bullet(self.rect.centerx, self.rect.top + 1)
        all_sprites.add(b)
        bullet_group.add(b)


class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom <0:
            self.kill()
           # print("kill")


class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (r.randint(25, WIDTH-25))
        self.rect.top = (0)
        self.speedy = r.randint(1,6)
        self.speedx = r.randint(-4,4)


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx



        if self.rect.right >= WIDTH-1 or self.rect.left<=0:
            self.speedx = self.speedx * -1
        if self.rect.top <=0 or self.rect.bottom>=HEIGHT+150:
            self.rect.y = 0

    def spawn(self):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)



####################################################################


# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60


# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

title = "Shmup"

####################################################################

# Folder Variables
####################################################################
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder,"imgs")
snds_folder = path.join(game_folder,"snds")
scores_folder = path.join(game_folder,"scores")
player_img_folder = path.join(imgs_folder, "player_imgs")
enemy_img_folder = path.join(imgs_folder, "enemy_imgs")
background_img_folder = path.join(imgs_folder, "backgrounds")
print(imgs_folder)
####################################################################

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################

# load imgs
####################################################################
background = pg.image.load(path.join(background_img_folder, "blue.png"))
####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
####################################################################

# create Game Objects
####################################################################
player = Player()
#npc = NPC()
for i in range(10):
    npc = NPC()
    npc_group.add(npc)


####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)



for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)

####################################################################


# Game Loop
###################
# game update Variables
########################################
playing = True

########################################
################################################################
while playing:
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################

    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
                # fluid movement
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                 player.speedx = -5
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player.speedx = 5
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                player.speedy = 5
            if event.key == pg.K_UP or event.key == pg.K_w:
                player.speedy = -5
            if event.key == pg.K_SPACE or event.key == pg.K_UP:
                player.shoot()
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                 player.speedx = 0
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player.speedx = 0
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                player.speedy = 0
            if event.key == pg.K_UP or event.key == pg.K_w:
                player.speedy = 0
        if event.type == pg.QUIT:
            playing = False



    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # if NPC hits player
    hits = pg.sprite.spritecollide(player,npc_group,True)
    if hits:
        npc.spawn()
        #playing = False
        print("player hit")
    # if bullet hits NPC
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        npc.spawn()
        print("bullet hit")

    #if NPC hits NPC
    # hits = pg.sprite.spritecollide(npc,npc_group,False)
    # for hit in hits:
    #     hit.speedx = -hit.speedx


    ##################################################
    # Render
    ##################################################

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()
    ##################################################

pg.quit()
################################################################
#####################