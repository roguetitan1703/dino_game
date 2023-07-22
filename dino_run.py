import pygame as py
import random

USEREVENT = 0
py.init()
i = 0
x = 0
game = True
bird_fly = [py.image.load('dino_image/bird_1.png'),py.image.load('dino_image/bird_2.png'),py.image.load('dino_image/bird_1.png'),py.image.load('dino_image/bird_2.png')]
dino_duck = [py.image.load('dino_image\dino_duck_1.png'),py.image.load('dino_image\dino_duck_2.png'),py.image.load('dino_image\dino_duck_1.png'),py.image.load('dino_image\dino_duck_2.png')]
dino_run = [py.image.load('dino_image\dino_b_up.png'), py.image.load('dino_image\dino_f_up.png'), py.image.load('dino_image\dino_b_up.png'), py.image.load('dino_image\dino_f_up.png')]
bg = py.image.load('dino_image/bg.png')
bgx = 0
jumplist = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
bgx2 = bg.get_width()
Win = py.display.set_mode((700,400))
walkright = False
walkleft = False
clock = py.time.Clock()
py.time.set_timer(USEREVENT+1,500)
speed = 30
x = 100
y = 337
neg = 1
cact = py.image.load('dino_image/obs_8.png')


class player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.runcount = 0
        self.running = True
        self.jumping = False
        self.jumpcount = 0
        self.ducking = False
        self.duckcount = 0
        self.list = dino_run
        self.crr = 0
    def run(self):
        if self.running == True:
            if self.runcount + 1 >160:
                self.runcount = 0
            Win.blit(dino_run[self.runcount//40], (self.x, self.y+self.crr))
            self.runcount += 1

    def duck(self):
        if self.ducking == True:
            self.running = False
            if self.duckcount +1 >160:
                self.duckcount = 0
            self.crr = 20
            Win.blit(dino_duck[self.duckcount//40], (self.x, self.y+self.crr))
            self.duckcount += 1
            self.list = dino_duck

        else:
            self.running = True
            self.ducking = False
            self.list = dino_run
            self.crr = 0





    def jump(self):
        if self.jumping == True:
            self.y -= jumplist[self.jumpcount]*1.3
            Win.blit(self.list[self.jumpcount//28],(self.x, self.y+self.crr))
            self.jumpcount += 1
            if self.jumpcount > 108:
                self.jumpcount = 0
                self.jumping = False
                self.running = True

class cactus(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.img = cact
    def draw(self):
        self.hitbox = ()
        Win.blit(self.img, (self.x, self.y))
        py.draw.rect(Win,(255, 0, 0), self.hitbox,2)


def play_game():
    global game, speed, bgx, bgx2, x, y, neg, cact, keys
    x = 100
    y = 337
    
    dino = player(x,y)
    while game:
        clock.tick(speed)
        keys = py.key.get_pressed()

        for event in py.event.get():
            if event.type == py.QUIT:
                game = False
            if event.type == USEREVENT+1:
                speed += 1
        if keys[py.K_SPACE]:
            dino.jumping = True
            dino.running = False
        if keys[py.K_DOWN]:
            dino.ducking = True
        else:
            dino.ducking = False





        Win.blit(bg, (bgx, 0))
        Win.blit(bg, (bgx2, 0))
        bgx -= 1
        bgx2 -= 1
        if bgx < bg.get_width() * -1:
            bgx = bg.get_width()
        if bgx2 < bg.get_width() * -1:
            bgx2 = bg.get_width()

        dino.jump()
        dino.duck()
        dino.run()
        py.display.update()

if __name__ == "__main__":
    play_game()