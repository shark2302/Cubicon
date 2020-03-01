import pygame, sys
from pygame.locals import *
from Player import Player
from LevelLoader import LevelLoader
from ColorBlock import ColorBlock
from Color import Color

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FPS = 30

def loadLevel(fileName) :
    f = open(fileName, "r")
    fileData = f.read().split();
    f.close()
    lvl = []
    for each in fileData :
        s = []
        for char in each :
            s.append(int(char))
        lvl.append(s)
    return lvl

def drawPlayer(player, screen) :
    x = 100 + player.getPos()[1] * 50
    y = 100 + player.getPos()[0] * 50
    pygame.draw.rect(screen, GRAY, (x + 2, y + 2, 46, 46), 3)
    pygame.draw.rect(screen, GRAY, (x + 7, y + 7, 36, 36), 3)

def drawLevel(lvl, screen) :
    x = 100
    y = 100
    for string in lvl :
        for each in string :
            if each == 1 :
                pygame.draw.rect(screen, GRAY, (x, y, 50, 50))
            if type(each) == ColorBlock :
                if each.getColor() == Color.PINK :
                    pygame.draw.rect(screen, PINK, (x, y, 50, 50))
                if each.getColor() == Color.BLUE :
                    pygame.draw.rect(screen, LIGHT_BLUE, (x, y, 50, 50))
            pygame.draw.rect(screen, BLACK, (x, y, 50, 50), 1)
            x+=50
        y += 50
        x = 100




pygame.init()
clock = pygame.time.Clock()
lvl = LevelLoader("levels/level1.txt")
player = lvl.getPlayer()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cubecon");
bgColor = (255,255,255)
mainLoop = True



while mainLoop:
    screen.fill(bgColor)
    drawLevel(lvl.getLevelMap(), screen)
    drawPlayer(player, screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                player.moveUp(lvl)
            if event.key == pygame.K_DOWN :
                player.moveDown(lvl)
            if event.key == pygame.K_RIGHT :
                player.moveRight(lvl)
            if event.key == pygame.K_LEFT :
                player.moveLeft(lvl)
    clock.tick(FPS)

pygame.quit()
