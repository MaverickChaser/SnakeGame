#!/usr/bin/env python2
import sys
import random
import time

from snake import *
from ai_snake import AISnake

FPS = 12

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

def genPrize(Y_CORD = 100):
    k = random.randint((-START_X + RADIUS) // DIAMETER + 2, (SCREEN_WIDTH - START_X + RADIUS) // DIAMETER - 2)
    l = random.randint((-Y_CORD + RADIUS) // DIAMETER + 2, (SCREEN_HEIGHT - Y_CORD + RADIUS) // DIAMETER - 2)
    x, y = 100 - RADIUS + k * DIAMETER, Y_CORD - RADIUS + l * DIAMETER
    prize = pygame.Rect(x, y, PRIZE_SIZE, PRIZE_SIZE)
    return prize

def drawText(s, color, font, x, y):
    text = font.render(s, True, color, BACKGROUND)
    text_rect = text.get_rect()
    text_rect.left, text_rect.top = x, y
    screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    pygame.display.update()
    running = 1

    prize = genPrize()
    pygame.draw.rect(screen, RED, prize)

    fPlayer = Snake(GREEN, 100, RIGHT[0], DOWN[0], LEFT[0], UP[0])
    sPlayer = AISnake(BLUE, 300, RIGHT[1], DOWN[1], LEFT[1], UP[1])

    state = ON

    ms_left, start = DURATION, time.time()
    winner = 0

    while running and ms_left and not winner:

        key1, key2 = None, None
        events = pygame.event.get()

        for e in events:
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif e.type == KEYDOWN:
                if e.key == ord('q'):
                    pygame.quit()
                    sys.exit(0)
                elif e.key == K_ESCAPE:
                    if state == ON:
                        state = PAUSE
                    elif state == PAUSE:
                        state = ON

            if e.type == KEYDOWN and state == ON:
                if fPlayer.changesState(e.key):
                    key1 = e.key
                elif sPlayer.changesState(e.key):
                    key2 = e.key

        #if key1 != None:
        #    fPlayer.changeDirection(key1)

        #if second player != AI
        #if e2 != None:
        #    sPlayer.changeDirection(e2)


        if state == ON:
            screen.fill((0, 0, 120))

            #for i in range(5):
            #    pygame.draw.rect(screen, SILVER, (random.randint(3, SCREEN_WIDTH), random.randint(3, SCREEN_HEIGHT), 2, 2))

            now = time.time()
            delta = now - start
            start = now

            ms_left -= int(delta * 1000)
            if ms_left < 0:
                ms_left = 0

            s, ms = ms_left // 1000, ms_left % 1000 // 10

            drawText(str(s) + '.' + str(ms), WHITE, timeFont, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            drawText("Score: {0}".format(fPlayer.score), fPlayer.color, scoreFont, SCORE_FIRST_X, SCORE_FIRST_Y)
            drawText("Score: {0}".format(sPlayer.score), sPlayer.color, scoreFont, SCORE_SECOND_X, SCORE_SECOND_Y)

            pygame.draw.rect(screen, RED, prize)

            if key1 is not None:
                fPlayer.changeDirection(key1)
            fPlayer.move()

            got = 0

            if fPlayer.foundPrize(prize):
                got = 1
                fPlayer.grow(sPlayer)

            sPlayer.changeDirection(fPlayer, prize)
            sPlayer.move()

            if not got and sPlayer.foundPrize(prize):
                got = 1
                sPlayer.grow(fPlayer)

            if fPlayer.isAlive(sPlayer):
                fPlayer.draw(screen)
            else:
                running = 0
                winner = 2
                #print 'green player lost'
                #print 'wtf? ', fPlayer.ax, fPlayer.ay
                fPlayer.draw(screen)

            if sPlayer.isAlive(fPlayer):
                sPlayer.draw(screen)
            else:
                running = 0
                #print 'blue player lost'
                #print 'wtf? ', sPlayer.ax, sPlayer.ay
                sPlayer.draw(screen)
                winner = 1

            if got:
                prize = genPrize()
                pygame.draw.rect(screen, RED, prize)

            pygame.display.update()

            #if not m_secs:
            #    pygame.time.delay(2000)

        else:
            start = time.time()
        clock.tick(FPS)

    if (fPlayer.score > sPlayer.score and not winner) or winner == 1:
        drawText('Green Player won!', GREEN, scoreFont, 150, 150)
    elif (sPlayer.score > fPlayer.score and not winner) or winner == 2:
        drawText('Blue Player won!', BLUE, scoreFont, 150, 150)
    else:
        drawText('Draw!', SILVER, scoreFont, 150, 150)

    pygame.display.update()

if __name__ == "__main__":
    main()
    quit = 0

    while not quit:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit = 1
            elif e.type == KEYUP:
                if e.key == ord('q'):
                    quit = 1
                    break
                elif e.key == ord('r'):
                    main()



