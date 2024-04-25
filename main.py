from pygame import *
from random import randint, choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
font.init()
font1 = font.SysFont('Arial', 36)
lost = 0
win = 0
HP = 3
font2 = font.SysFont('Arial', 50)
window = display.set_mode((500,500))
display.set_caption('Maze')
background = transform.scale(image.load("images.jpeg"),(500,500))
fake = True
run = True
clock = time.Clock()
FPS = 60
finish1 = False
finish2 = False
finish3 = False
win1 = 0
win2 = 0
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_weight,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_weight, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))        
player1 = GameSprite('player1.jpeg',50,250,150,150)
player2 = GameSprite('player2.jpeg',50,250,150,150)
player3 = GameSprite('player3.jpeg',50,250,150,150)
player4 = GameSprite('player1.jpeg',300,250,150,150)
player5 = GameSprite('player2.jpeg',300,250,150,150)
player6 = GameSprite('player3.jpeg',300,250,150,150)
enemy = choice([player4,player5,player6])
while run:
    if fake == True:
        window.blit(background,(0,0))
        text_loby = font2.render('НАЧАТЬ ИГРУ', 1, (0,255,0))
        window.blit(text_loby,(100,200))
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_w:
                    fake = False
                    finish1 = True
                if e.key == K_s:
                    fake = False
                    finish2 = True
                if e.key == K_x:
                    fake = False
                    finish3 = True
    for e in event.get():
            if e.type == QUIT:
                run= False
    if finish1 != False:
        window.blit(background,(0,0))
        player1.reset()
        enemy.reset()
        if enemy == player5:
            text_win = font2.render('ПОБЕДА', 1, (0,255,0))
            finish1 = False
            window.blit(text_win,(100,200))
        if enemy == player4:
            text_norm = font2.render('НИЧЬЯ', 1, (0,255,0))
            finish1 = False
            window.blit(text_norm,(100,200))
        if enemy == player6:
            text_lose = font2.render('ПОРАЖЕНИЕ', 1, (0,255,0))
            finish1 = False
            window.blit(text_lose,(100,200))
        
    if finish2 != False:
        window.blit(background,(0,0))
        player2.reset()
        enemy.reset()
        if enemy == player6:
            text_win = font2.render('ПОБЕДА', 1, (0,255,0))
            finish1 = False
            window.blit(text_win,(100,200))
        if enemy == player5:
            text_norm = font2.render('НИЧЬЯ', 1, (0,255,0))
            finish1 = False
            window.blit(text_norm,(100,200))
        if enemy == player4:
            text_lose = font2.render('ПОРАЖЕНИЕ', 1, (0,255,0))
            finish1 = False
            window.blit(text_lose,(100,200))
        
    if finish3 != False:
        window.blit(background,(0,0))
        player3.reset()
        enemy.reset()
        if enemy == player4:
            text_win = font2.render('ПОБЕДА', 1, (0,255,0))
            finish1 = False
            window.blit(text_win,(100,200))
        if enemy == player6:
            text_norm = font2.render('НИЧЬЯ', 1, (0,255,0))
            finish1 = False
            window.blit(text_norm,(100,200))
        if enemy == player5:
            text_lose = font2.render('ПОРАЖЕНИЕ', 1, (0,255,0))
            finish1 = False
            window.blit(text_lose,(100,200))
    clock.tick(FPS)
    display.update()