import pygame
import time
from random import randrange
pygame.init()
x_dis = 1400
y_dis = 800
dis_weight_height = (x_dis, y_dis)
display = pygame.display.set_mode(dis_weight_height, pygame.FULLSCREEN)
pygame.display.set_caption('Go to down')
logo = pygame.image.load("images\logo.png")
pygame.display.set_icon(logo)

player_image = [pygame.image.load('images\stoy_user.png'), pygame.image.load('images\lstop.png'),pygame.image.load('images\lgo1.png'),pygame.image.load('images\lgo2.png'),pygame.image.load('images\pstop.png'),pygame.image.load('images\pgo1.png'),pygame.image.load('images\pgo2.png'), pygame.image.load('images\shootl.png'),pygame.image.load('images\shootp.png'), pygame.image.load('images\jump.png')]
other_image = [pygame.image.load('images\life.png'), pygame.image.load('images\пусто.png')]
objects = [pygame.image.load('images\пол.png'), pygame.image.load(r'images\bullet.png'), pygame.image.load(r'images\bulr.png'), pygame.image.load(r'images\bull.png')]
enemies = [pygame.image.load('images\глаз (1).png'), pygame.image.load('images\глаз (2).png'),pygame.image.load('images\глаз (3).png'), pygame.image.load('images\пти1.png'),pygame.image.load('images\пти2.png'), pygame.image.load(r'images\bulmon.png')]
cherep = [pygame.image.load('images\череп.png'),pygame.image.load('images\череп2.png')]
end = pygame.image.load('images\end.png')
w_player = 64
h_player = 64



x_glaz = 1000
y_glaz = 400
d = True
chey_hod_glaz = 1
g1 = True
x_player, y_player = 400, 500
play = True
FPS = pygame.time.Clock()
gun1go = False
gun2go = False
count_bullet = 40
jump = False
jump_c = 20
life_s = 71
count_life = 3
q = False
e = False
gun1 = gun2 = False
step2 = False
chered = 1
one = True
x_bul = 0
y_bul = 0
doshlo = True
what_bul = other_image[1]

def map_glaz(x_glaz, chey_hod_glaz):
    if x_glaz<1300 and chey_hod_glaz == 1:
        x_glaz += 2
        if x_glaz == 1300:
            chey_hod_glaz = 2
    if x_glaz>600 and chey_hod_glaz == 2:
        x_glaz -= 2
        if x_glaz == 600:
            chey_hod_glaz = 1
    return x_glaz, y_glaz, chey_hod_glaz

can = True
x_bul_m = x_glaz
y_bul_m = y_glaz+32
def gun_monst(x_glaz, x_bul_m, glaz):
    global can
    if can:
        x_bul_m = x_glaz + 32
        can = False
    if glaz == enemies[2]:
        x_bul_m -= 4
    elif glaz == enemies[1]:
        x_bul_m += 4
    if x_bul_m<0 or x_bul_m>x_dis:
        can = True
        x_bul_m = x_glaz
    return x_bul_m
#y1,h1,w1,y2, h1


def touch(x1, x2, w1,x_glaz, life_s, y1, y2):
    k = False
    if x1+w1>x2 and x1<x2 and y1+64>=y2 and y1<=y2:
        life_s -= 30
        k = True
    return life_s, x_glaz, k






y_cher = 500
x_cher = 800
obratno = False
color = (123, 172, 212)
count = y_player


start = pygame.image.load('images\start.png')
tik = 0
while play:
    rezerv = (x_player, y_player)
    display.fill(color)

    playerimage = player_image[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if chered%10 < 5:
            playerimage = player_image[2]
        else: playerimage = player_image[3]

        if e or q: x_player -= 0.5
        else: x_player -= 2


        chered+=1
        if x_player < 0:
            x_player = 0

    if keys[pygame.K_d]:
        if chered%10 >= 5: playerimage = player_image[5]
        else: playerimage = player_image[6]
        chered+=1
        if e or q: x_player += 0.5
        else: x_player += 2
        if x_player > x_dis-w_player:
            x_player = x_dis-w_player

    if keys[pygame.K_LEFT]:
        playerimage = player_image[7]
        q = True
        gun1 = True
        if gun2go!=True:
            gun1go = True
    else:
        gun1 = False
        q = False
    if keys[pygame.K_RIGHT]:
        playerimage = player_image[8]
        e = True
        gun2 = True
        if gun1go!=True:
            gun2go = True
    else:
        gun2 = False
        e = False


    if keys[pygame.K_ESCAPE]: play = False



    if keys[pygame.K_w]:
        y_player -= 2

        if y_player < 0:
          y_player = 0

    if keys[pygame.K_w]:
        jump = True
     #   if y_player < 0:
      #      y_player = 0
    if keys[pygame.K_s]:
        y_player += 2
        count += 2
    if y_player > y_dis-h_player:
        y_player = y_dis-h_player
    if jump:
        playerimage = player_image[9]
        if jump_c > -24:
            y_player -= jump_c//2.5
            jump_c -= 1
        else:
            jump = False
            jump_c = 20



    display.blit(what_bul, (x_bul, y_bul))
    if keys[pygame.K_SPACE] and (gun1 or gun2) and count_bullet>0 and doshlo:
        x_bul = x_player + 32
        y_bul = y_player + 9

        step2 = True

        count_bullet -= 1
        doshlo = False

    if gun1go and step2:
        what_bul = objects[3]
        x_bul -= 40

        if x_bul<0:
            gun1 = False
            doshlo = True
            gun1go = False
            step2 = False
            if count_bullet == 0:
                what_bul = other_image[1]
    if gun2go and step2:
        what_bul = objects[2]
        x_bul += 40

        if x_bul>x_dis:
            gun2 = False
            doshlo = True
            gun2go = False
            step2 = False
            if count_bullet == 0:
                what_bul = other_image[1]


    if x_player > 205 and x_player < 635:
        if y_player>186 and y_player<274:
            x_player = rezerv[0]
            y_player = rezerv[1]
    display.blit(objects[0], (250, 250))

    display.blit(playerimage, (x_player, y_player))





    otherimage = other_image[0]
    life = [display.blit(otherimage, (i, 20)) for i in range(10, life_s, 30) if life_s > 0]
    bullet = [display.blit(objects[1], (i+101, 20)) for i in range(10, count_bullet*30+1, 30)]

    life_s, x_glaz, k = touch(x_player, x_bul_m, 32, x_glaz, life_s, y_player, y_bul_m)
    if k:
        x_bul_m = x_glaz
    if not(life):
        #display.fill(color)
        display.blit(end, (x_dis / 2 - 215, y_dis / 2 - 50))
        if tik == -1:
            exit()
    else:
        if d:
            lol = start
            d = False


    x_glaz, y_glaz, chey_hod_glaz = map_glaz(x_glaz, chey_hod_glaz)
    if abs(x_player-x_glaz) < 100:
        glaz = enemies[0]
    elif x_glaz<x_player:
        glaz = enemies[1]
    else:
        glaz = enemies[2]
    if tik == 200:
        lol = other_image[1]


    if x_player>x_cher:
        cher = cherep[0]
    else: cher = cherep[1]







    x_bul_m = gun_monst(x_glaz, x_bul_m, glaz)
    display.blit(cher, (x_cher, y_cher))
    display.blit(enemies[5], (x_bul_m, y_bul_m))
    display.blit(enemies[3], (1000, 200))
    display.blit(glaz, (x_glaz, y_glaz))
    display.blit(lol, (x_dis / 2 - 215, y_dis / 2 - 50))
    pygame.display.update()
    FPS.tick(60)
    if tik != -1 and obratno and not(life):
        tik -= 1

  #  tik += 1
    if tik != 202 and not(obratno):
        tik += 1
        if tik == 202:
            tik = 199
            obratno = True
    print(tik)
pygame.quit()
