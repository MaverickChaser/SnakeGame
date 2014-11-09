from Queue import Queue

import snake
from config import *

INF = int(1e9)


def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1


class AISnake(snake.Snake):

    def isSurrounded(self, enemy):
        moves = MOVES
        emptyCells = Queue()
        head = self.getHead()
        emptyCells.put(head)

        visited = set(self.queue[1:] + enemy.queue)

        while moves and not emptyCells.empty():
            size = emptyCells.qsize()
            #if size == 1 and moves < MOVES:
            #    return 1
            while size:
                cell = emptyCells.get()
                for i, j in directions:
                    ncell = cell[0] + i * DIAMETER, cell[1] + j * DIAMETER
                    if ncell not in visited and not isOutside(ncell):
                        visited.add(ncell)
                        emptyCells.put(ncell)
                        #print ncell

                size -= 1

            moves -= 1

        return emptyCells.empty()

    def checkDirection(self, enemy, prize=None, bx=None, by=None):

        if bx is None:
            bx, by = self.ax, self.ay

        curx, cury = self.ax, self.ay
        self.ax, self.ay = bx, by
        was = self.queue
        self.move()
        can_go = self.isAlive(enemy) and not self.isSurrounded(enemy)
        dist = INF

        if prize is not None and can_go:
            dist = getDist(self.getHead(), (prize.centerx, prize.centery))

        self.queue = was
        self.ax, self.ay = curx, cury

        return can_go, dist

    def changeDirection(self, snake, prize):
        curx, cury = self.ax, self.ay
        changeX = (curx != 0)
        found, ansx, ansy = 0, self.ax, self.ay

        curdir = self.checkDirection(snake, prize)
        found = curdir[0]
        curdist = curdir[1] if found else INF

        for d in (-1, 1):
            curx, cury = (0, dy * d) if changeX else (dx * d, 0)
            take, ndist = self.checkDirection(snake, prize, curx, cury)

            if take and (not found or ndist < curdist):
                found = 1
                curdist = ndist
                ansx, ansy = curx, cury


        #if not found:
        #    print 'fail ', self.color
            #self.changeDirection(snake, prize)
        #    print self.__repr__()

        self.ax, self.ay = ansx, ansy


