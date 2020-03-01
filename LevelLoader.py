from Player import Player
from Color import Color
from ColorBlock import ColorBlock
class LevelLoader :


    def __init__(self, fileName) :
        self.fileName = fileName
        self.levelMap = None
        self.player = None
        def createLevelMap() :
            f = open(self.fileName, "r")
            fileData = f.read().split();
            f.close()
            lvl = []
            for each in fileData :
                s = []
                for char in each :
                    s.append(int(char))
                    if int(char) == 4 :
                        self.player = Player(fileData.index(each), s.index(int(char)))
                        index = s.index(int(char))
                        s.remove(int(char))
                        s.insert(index, 0)
                    if int(char) == 2 :
                        index = s.index(int(char))
                        s.remove(int(char))
                        s.insert(index, ColorBlock(fileData.index(each), index, Color.PINK))
                    if int(char) == 3 :
                        index = s.index(int(char))
                        s.remove(int(char))
                        s.insert(index, ColorBlock(fileData.index(each), index, Color.BLUE))
                lvl.append(s)
            self.levelMap = lvl
        createLevelMap()



    def getLevelMap(self) :
        return self.levelMap

    def getPlayer(self) :
        return self.player
