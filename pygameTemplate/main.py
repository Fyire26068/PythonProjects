import math
import pygame
import random
import sys
import colors as c

WIDTH = 640
HEIGTH = 480
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()




class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGTH/2)
        #self.rect.bottomright = (0,0)
        self.speedx = 6
        self.speedy = 6
        self.ang = 0
        self.do_Circle = False



    def update(self):

        # movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right >= WIDTH-1 or self.rect.left<=0:
            self.speedx = self.speedx * -1
        if self.rect.top <=0 or self.rect.bottom>=HEIGTH-1:
            self.speedy = self.speedy * -1


        # #square movement
        # if self.rect.right >= WIDTH-1:
        #     self.speedx = 0
        #     self.speedy = -5
        # if self.rect.top <= 1:
        #     self.speedx = -5
        #     self.speedy = 0
        # if self.rect.left <= 1:
        #     self.speedx = 0
        #     self.speedy = 5
        # if self.rect.bottom >= HEIGTH-1:
        #     self.speedx = 5
        #     self.speedy = 0

        # # enemy movement pattern
        # if self.rect.centerx >= WIDTH/2:
        #     self.do_Circle = True
        #     if self.do_Circle:
        #         if self.ang <360:
        #             rad = self.ang * math.pi / 180
        #             self.rect.centery = -math.sin(rad) * 5 + self.rect.centery
        #             self.rect.centerx = math.cos(rad) * 5 + self.rect.centerx
        #             self.ang += 20
        #         else:
        #             self.do_Circle = False
        #     self.speedx = 5
        #     self.speedy = -5
        # if self.rect.bottomleft[0]>WIDTH and self.rect.bottomleft[1]<=0:
        #     self.rect.bottomright = (0,0)
        #     self.speedx = 5
        #     self.speedy = 5
        #     self.ang = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(c.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGTH / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy



#sprite groups
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()

# create game objects
npc = Npc()
player = Player()

# add to groups
all_sprites.add(npc)
mobs_group.add(npc)
all_sprites.add(player)
players_group.add(player)




#game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # grid movement
            if event.key == pygame.K_LEFT:
                player.rect.x += -50
            if event.key == pygame.K_RIGHT:
                player.rect.x += 50
            if event.key == pygame.K_DOWN:
                player.rect.y += 50
            if event.key == pygame.K_UP:
                player.rect.y += -50


        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    #process input


    #update
    all_sprites.update()


    #draw
    screen.fill(c.BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

