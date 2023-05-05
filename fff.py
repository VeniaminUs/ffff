from pygame import *
from random import randint
from time import time as timer

img_back = 'galaxy.jpg'
img_hero = 'platform.png'
img_enemy = 'ufo.png'
img_bullet = "Ball.png"
img_asteroid = 'asteroid.png'
# score = 0
# lost = 0
# max_lost = 10
# goal = 25
# num_fire = 0
# lifes = 3


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 120:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 120:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width-80)
            self.rect.y = 0
            if self.size_x == 80:
                lost += 1



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')


raket1 = Player(img_hero, 10, 188, 25, 130, 10)
raket2 = Player(img_hero, 640, 188, 25, 130, 10)


run = True
finish = False
rel_time = False
clock = time.Clock()
FPS = 30

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')

font.init()
font1 = font.SysFont("Areal", 80)
win1 = font1.render("Победил игрок 1", True, (255, 255, 255))
win2 = font1.render('Победил игрок 2', True, (180, 0, 0))
font2 = font.SysFont("Areal", 36)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        

    if finish != True:
        window.fill((255, 255, 255))

        raket1.update_L()
        raket2.update_R()

        raket1.reset()
        raket2.reset()
        display.update()

    time.delay(FPS) 