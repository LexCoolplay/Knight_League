from pygame.locals import *
import pygame
import os
from Hero import Hero
from Wall import Wall

left=right=up=down=False
game_loop=1
resolution=tuple((800,640))
WALL_WIDTH = 32;
WALL_HEIGHT = 32;
WALL_COLOR ="#FF6262"

pygame.init()
display=pygame.display
display.init()
screen = display.set_mode(resolution)
event=pygame.event
bg=pygame.Surface(resolution)
bgColor= (255,255,255)
bg.fill(Color("#004400"))
x,y=0,0
clock=pygame.time.Clock()
dic={0:0,1:0,2:0,3:0}
image=pygame.image.load(os.path.join("PlayerTest.png"))
hero=Hero(image,55,55)


entities = pygame.sprite.Group()
platforms= []
level= [
    "----------     ----------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-                       -",
    "-------------------------",
]
entities.add(hero)
left=right=up=down=False

while game_loop:
    clock.tick(120)

    x=y=0;
    for row in level:
        for col in row:
            if col == "-":
                pf=Wall(x,y)
                entities.add(pf)
                platforms.append(pf)
            x += WALL_WIDTH
        y += WALL_HEIGHT
        x=0;
    for i in event.get():
        if i.type == QUIT:
            game_loop=False
        if i.type == KEYDOWN and i.key == K_UP:
            up=True
        if i.type == KEYDOWN and i.key == K_DOWN:
            down=True
        if i.type == KEYDOWN and i.key == K_LEFT:
            left=True
        if i.type == KEYDOWN and i.key == K_RIGHT:
            right=True
        if i.type == KEYUP and i.key == K_UP:
            up=False
        if i.type == KEYUP and i.key == K_DOWN:
            down=False
        if i.type == KEYUP and i.key == K_LEFT:
            left=False
        if i.type == KEYUP and i.key == K_RIGHT:
            right=False
        #print(i)
    screen.blit(image, (0, 0))
    #screen_layer
    screen.blit(bg, (0, 0))
    #entity_layer
    screen.fill(bgColor)
    hero.update(left, right, up, down,platforms)
    entities.draw(screen)
    pygame.display.update()




