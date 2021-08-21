# import os
# abs_path = os.path.abspath(__file__)
# os.chdir(os.path.dirname(abs_path))
from pygame import *
from random import randint
from time import time as timer, sleep
# Classes
class Sprites(sprite.Sprite):
    def __init__(self, image1, x1, y1, size1, size2, speed1):
        super().__init__()

        self.image = transform.scale(image.load(image1), (size1, size2))
        self.speed = speed1

        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Players(Sprites):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 430:
            self.rect.y += 5

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += 5

class NPC(Sprites):
    pass

# The whole program:
w1 = 700
h1 = 500
window = display.set_mode((w1, h1))
display.set_caption("A Ping Pong Game")
window.fill((0, 0, 170))

# The Sprites
paddle1 = Players("racket.png", 5, 250, 30, 70, 5)
paddle2 = Players("racket.png", 650, 250, 30, 70, 5)


# Running the game
run = True
clock = time.Clock()
fps = 60
finished = False
lives = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finished:
        window.fill((0, 0, 170))

        paddle1.update1()
        paddle2.update2() 
        
        paddle1.reset()
        paddle2.reset()
        

    # Collision detection to end the game
    # If blahblahblah reaches/collides with blahblahblah

    display.update()
    clock.tick(fps)