import math
import pygame
import random
import os
import sys
import colors as c

#setup folder Assets
game_folder =os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"imgs")
snd_folder = os.path.join(game_folder,"snds")



WIDTH = 640
HEIGTH = 480
FPS = 60
title = "template"







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

        # screen wrapping
        # if self.rect.left > WIDTH:
        #    self.rect.right = 0
        # if self.rect.right < 0:
        #    self.rect.left = WIDTH
        # if self.rect.top < 0:
        #    self.rect.bottom = HEIGHT
        # if self.rect.bottom > HEIGHT:
        #    self.rect.top = 0

        # if self.rect.left > WIDTH:
        #     self.rect.right = WIDTH / 2
        #     self.rect.bottom = HEIGHT
        #     self.speedx = 0
        #     self.speedy = -5
        # if self.rect.top < 0:
        #     self.rect.bottom = HEIGHT / 2
        #     self.rect.right = WIDTH
        #     self.speedx = -5
        #     self.speedy = 0
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH / 2
        #     self.rect.top = 0
        #     self.speedx = 0
        #     self.speedy = 5
        # if self.rect.bottom > HEIGHT:
        #     self.rect.top = HEIGHT / 2
        #     self.rect.left = 0
        #     self.speedx = 5
        #     self.speedy = 0

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
        #self.image = pygame.Surface((50, 50))
        self.image = player_img
        self.image.fill(c.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGTH / 2)
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False

    def update(self):
        # movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #self.rect.center = (mousex, mousey)


        # keystate = pygame.key.get_pressed()
        # if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += -50
        # if (keystate[pygame.K_RIGHT] or keystate[pygame.K_d]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += 50
        # if (keystate[pygame.K_UP] or keystate[pygame.K_w]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += -50
        # if (keystate[pygame.K_DOWN] or keystate[pygame.K_s]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += 50
        # keyrelease = pygame.KEYUP
        # if keyrelease:
        #     self.keypressed = False


        # bind player to screen
        if self.rect.left > WIDTH:
           self.rect.left = WIDTH - 25
        if self.rect.right < 0:
           self.rect.right = 0 + 25
        if self.rect.top < 0:
           self.rect.top = 0
        if self.rect.bottom > HEIGTH:
           self.rect.bottom = HEIGTH



        # screen wrapping
        # if self.rect.left > WIDTH:
        #    self.rect.right = 0
        # if self.rect.right < 0:
        #    self.rect.left = WIDTH
        # if self.rect.top < 0:
        #    self.rect.bottom = HEIGTH
        # if self.rect.bottom > HEIGTH:
        #    self.rect.top = 0

    def toggle_pressed(self):
        self.keypressed = False

def spw_newPlayers(x,y):
   newPlayer = Player(x,y)
   newPlayer.image = pygame.Surface((50, 50))
   newPlayer.image.fill(c.BLUE)
   newPlayer.rect = newPlayer.image.get_rect()
   newPlayer.rect.center = (x,y)


pygame.init()
pygame.mixer.init()

#load in game imgs
player_img = pygame.image.load(os.path.join(img_folder,"char.png"))


screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()



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

    mousex,mousey = pygame.mouse.get_pos()
    mouse_buttn_held = False
    #print(mousex, mousey)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_buttn_held = True

            print("clicked on player")

        if event.type == pygame.MOUSEBUTTONUP and mouse_buttn_held == True:
            mouse_buttn_held = False
            spw_newPlayers(mousex, mousey)


        if event.type == pygame.KEYDOWN:

            # grid movement
            # if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP4:
            #     player.rect.x += -50
            # if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP6:
            #     player.rect.x += 50
            # if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP2:
            #     player.rect.y += 50
            # if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP8:
            #     player.rect.y += -50
            # if event.key == pygame.K_KP7:
            #     player.rect.x += -50
            #     player.rect.y += -50
            # if event.key == pygame.K_KP9:
            #     player.rect.x += 50
            #     player.rect.y += -50
            # if event.key == pygame.K_KP1:
            #     player.rect.x += -50
            #     player.rect.y += 50
            # if event.key == pygame.K_KP3:
            #     player.rect.x += 50
            #     player.rect.y += 50


            # fluid movement
            # if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #     player.speedx = -5
            # if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #     player.speedx = 5
            # if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #     player.speedy = 5
            # if event.key == pygame.K_UP or event.key == pygame.K_w:
            #     player.speedy = -5


            # escape exit key
            if event.key == pygame.K_ESCAPE:
                running = False


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.speedx = 0
                player.togglepressed()
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.speedy = 0
                player.togglepressed()


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

