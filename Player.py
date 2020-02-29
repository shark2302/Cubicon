class Player :

    def __init__(self, posX, posY) :
        self.posX = posX;
        self.posY = posY;

    def moveUp(self, lvl) :
        if lvl[self.posX - 1][self.posY] != 1 :
            self.posX -= 1

    def moveDown(self, lvl) :
        if lvl[self.posX + 1][self.posY] != 1 :
            self.posX += 1

    def moveRight(self, lvl) :
        if lvl[self.posX][self.posY + 1] != 1 :
            self.posY += 1

    def moveLeft(self, lvl) :
        if lvl[self.posX][self.posY - 1] != 1 :
            self.posY -= 1

    def getPos(self) :
        return [self.posX, self.posY]
