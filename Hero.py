from GameObject import GameObject
from pygame import *

MOVE_SPEED = 7

class Hero(GameObject):
    def __init__(self,source,x,y):
        #super().__init__(source,x,y)
        self.xvel=0
        self.yvel=0
        self.startX = x
        self.startY = y
        WIDTH = 22
        HEIGHT = 32
        COLOR = "#888888"
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x,y, WIDTH, HEIGHT)

        self.rect =Rect(x,y,WIDTH,HEIGHT)
    def update(self,left,right,up,down,platforms):
        #print(left,right,up,down)
        if left:
            self.xvel= -MOVE_SPEED
        if right:
            self.xvel= MOVE_SPEED
        if up:
            self.yvel= -MOVE_SPEED
        if down:
            self.yvel= MOVE_SPEED
        if not (right or left):
            self.xvel=0
        if not (up or down):
            self.yvel=0
        self.rect.x += self.xvel
        self.collide(0,self.yvel,platforms)
        self.rect.y += self.yvel
        self.collide(self.xvel,0,platforms)
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
    def collide(self,xvel,yvel,platforms):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if(xvel>0):

                    self.rect.right=p.rect.left
                if(xvel<0):

                    self.rect.left=p.rect.right
                if(yvel>0):

                    #self.rect.bottom=p.rect.top
                if(yvel<0):

                    #self.rect.top=p.rect.bottom
