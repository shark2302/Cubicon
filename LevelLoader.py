from Player import Player
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
                lvl.append(s)
            self.levelMap = lvl
        createLevelMap()



    def getLevelMap(self) :
        return self.levelMap

    def getPlayer(self) :
        return self.player
