from ColorBlock import ColorBlock
class Player :

    def __init__(self, posX, posY) :
        self.posX = posX;
        self.posY = posY;

    def moveUp(self, lvl) :
        if lvl.getLevelMap()[self.posX - 1][self.posY] == 0 :
            self.posX -= 1
        elif type(lvl.getLevelMap()[self.posX - 1][self.posY]) == ColorBlock and lvl.getLevelMap()[self.posX - 2][self.posY] == 0 :
            print(lvl.getLevelMap())
            lvl.getLevelMap()[self.posX - 1][self.posY].moveUp(lvl)
            self.posX -= 1
            print(lvl.getLevelMap())

    def moveDown(self, lvl) :
        if lvl.getLevelMap()[self.posX + 1][self.posY] == 0 :
            self.posX += 1
        elif type(lvl.getLevelMap()[self.posX + 1][self.posY]) == ColorBlock and lvl.getLevelMap()[self.posX + 2][self.posY] == 0 :
            lvl.getLevelMap()[self.posX + 1][self.posY].moveDown(lvl)
            self.posX += 1


    def moveRight(self, lvl) :
        if lvl.getLevelMap()[self.posX][self.posY + 1] == 0 :
            self.posY += 1
        elif type(lvl.getLevelMap()[self.posX][self.posY + 1]) == ColorBlock and lvl.getLevelMap()[self.posX][self.posY + 2] == 0 :
            lvl.getLevelMap()[self.posX][self.posY + 1].moveRight(lvl)
            self.posY += 1

    def moveLeft(self, lvl) :
        if lvl.getLevelMap()[self.posX][self.posY - 1] == 0 :
            self.posY -= 1
        elif type(lvl.getLevelMap()[self.posX][self.posY - 1]) == ColorBlock and lvl.getLevelMap()[self.posX][self.posY - 2] == 0 :
            lvl.getLevelMap()[self.posX][self.posY - 1].moveLeft(lvl)
            self.posY -= 1

    def getPos(self) :
        return [self.posX, self.posY]
