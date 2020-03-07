import pygame, sys
from pygame.locals import *
from Player import Player
from LevelLoader import LevelLoader
from ColorBlock import ColorBlock
from Color import Color
from Button import Button

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
                if each.getColor() == Color.YELLOW :
                    pygame.draw.rect(screen, YELLOW, (x, y, 50, 50))
                if each.getColor() == Color.GREEN :
                    pygame.draw.rect(screen, GREEN, (x, y, 50, 50))
            if each != 0 :
                pygame.draw.rect(screen, BLACK, (x, y, 50, 50), 1)
            x+=50
        y += 50
        x = 100

def stringSearch(lvl, color) :
    for string in lvl.getLevelMap() :
        for num in string :
            if type(num) == ColorBlock and num.getColor() == color:
                i = string.index(num) + 1
                s = []
                s.append(num)
                while type(lvl.getLevelMap()[lvl.getLevelMap().index(string)][i]) == ColorBlock and lvl.getLevelMap()[lvl.getLevelMap().index(string)][i].getColor() == color :
                    s.append(lvl.getLevelMap()[lvl.getLevelMap().index(string)][i])
                    i += 1
                if len(lvl.getColorBlocks().get(color)) == len(s) :
                    return True
                continue
    return False

def colomnSearch(lvl, color) :
    for i in range(len(lvl.getLevelMap()[0])) :
        for j in range(len(lvl.getLevelMap())) :
            if type(lvl.getLevelMap()[j][i]) == ColorBlock and lvl.getLevelMap()[j][i].getColor() == color :
                k = j + 1
                s = []
                s.append(lvl.getLevelMap()[j][i])
                while type(lvl.getLevelMap()[k][i]) == ColorBlock and lvl.getLevelMap()[k][i].getColor() == color :
                    s.append(lvl.getLevelMap()[k][i])
                    k += 1
                    if len(lvl.getColorBlocks().get(color)) == len(s) :
                        return True
                    break
    return False


def checkWin(lvl) :
    for color in lvl.getColorBlocks().keys() :
        if len(lvl.getColorBlocks().get(color)) == 0 :
            continue
        if stringSearch(lvl, color) == False and colomnSearch(lvl, color) == False:
            return False
    return True

pygame.init()
clock = pygame.time.Clock()
lvl = LevelLoader()
lvl.loadLevel(1)
player = lvl.getPlayer()
colorBlocks = lvl.getColorBlocks()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cubecon");
bgColor = (255,255,255)
mainLoop = True
levelNum = 1
restartButton = Button(GREEN, 5, 5, 100, 50, "Restart");
nextLvlBtn = Button(GREEN, 110, 5, 100, 50, "Next")
prevLvlBtn = Button(GREEN, 220, 5,100, 50, "Prev")

while mainLoop:
    if checkWin(lvl):
        levelNum += 1
        lvl.loadLevel(levelNum)
        player = lvl.getPlayer()


    screen.fill(bgColor)
    restartButton.draw(screen, (0, 0, 0))
    nextLvlBtn.draw(screen, (0,0,0))
    prevLvlBtn.draw(screen, (0,0,0))
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
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if restartButton.isOver(pygame.mouse.get_pos()) :
                lvl.loadLevel(1)
                player = lvl.getPlayer();
            if nextLvlBtn.isOver(pygame.mouse.get_pos()) and levelNum < 2 :
                levelNum += 1
                lvl.loadLevel(levelNum)
                player = lvl.getPlayer();
            if prevLvlBtn.isOver(pygame.mouse.get_pos()) and levelNum != 1 :
                levelNum -= 1
                lvl.loadLevel(levelNum)
                player = lvl.getPlayer();
    clock.tick(FPS)

pygame.quit()
