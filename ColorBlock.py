class ColorBlock :

    def __init__(self, posX, posY, color) :
        self.posX = posX
        self.posY = posY
        self.color = color


    def moveUp(self, lvl) :
        lvl.getLevelMap()[self.posX - 1][self.posY] = self
        lvl.getLevelMap()[self.posX][self.posY] = 0

    def moveDown(self, lvl) :
        lvl.getLevelMap()[self.posX + 1][self.posY] = self
        lvl.getLevelMap()[self.posX][self.posY] = 0

    def moveRight(self, lvl) :
        lvl.getLevelMap()[self.posX][self.posY + 1] = self
        lvl.getLevelMap()[self.posX][self.posY] = 0

    def moveLeft(self, lvl) :
        lvl.getLevelMap()[self.posX][self.posY - 1] = self
        lvl.getLevelMap()[self.posX][self.posY] = 0

    def getColor(self) :
        return self.color

    def getPos(self) :
        return [self.posX, self.posY]
