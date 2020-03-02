from Player import Player
from Color import Color
from ColorBlock import ColorBlock
class LevelLoader :


    def __init__(self) :
        self.levelMap = None
        self.player = None
        self.colorBlocks = {Color.PINK : [], Color.BLUE : [], Color.YELLOW : [], Color.GREEN : []}



    def loadLevel(self, levelNum) :
        self.player = None
        self.colorBlocks.get(Color.PINK).clear()
        self.colorBlocks.get(Color.BLUE).clear()
        self.colorBlocks.get(Color.YELLOW).clear()
        self.colorBlocks.get(Color.GREEN).clear()
        f = open("levels/level{}.txt".format(levelNum), "r")
        fileData = f.read().split();
        f.close()
        lvl = []
        for each in fileData :
            s = []
            for char in each :
                s.append(int(char))
                if int(char) == 9 :
                    self.player = Player(fileData.index(each), s.index(int(char)))
                    index = s.index(int(char))
                    s.remove(int(char))
                    s.insert(index, 0)
                if int(char) == 2 :
                    index = s.index(int(char))
                    s.remove(int(char))
                    cb = ColorBlock(fileData.index(each), index, Color.PINK)
                    s.insert(index, cb)
                    self.colorBlocks.get(cb.getColor()).append(cb)
                if int(char) == 3 :
                    index = s.index(int(char))
                    s.remove(int(char))
                    cb = ColorBlock(fileData.index(each), index, Color.BLUE)
                    s.insert(index, cb)
                    self.colorBlocks.get(cb.getColor()).append(cb)
                if int(char) == 4 :
                    index = s.index(int(char))
                    s.remove(int(char))
                    cb = ColorBlock(fileData.index(each), index, Color.YELLOW)
                    s.insert(index, cb)
                    self.colorBlocks.get(cb.getColor()).append(cb)
                if int(char) == 5 :
                    index = s.index(int(char))
                    s.remove(int(char))
                    cb = ColorBlock(fileData.index(each), index, Color.GREEN)
                    s.insert(index, cb)
                    self.colorBlocks.get(cb.getColor()).append(cb)
            lvl.append(s)
        self.levelMap = lvl
        print(self.player.getPos())

    def getColorBlocks(self) :
        return self.colorBlocks

    def getLevelMap(self) :
        return self.levelMap

    def getPlayer(self) :
        return self.player
