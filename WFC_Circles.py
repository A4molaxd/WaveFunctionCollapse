import pygame
import random

pygame.init()

WIDTH = 1280
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

size = 10

# [N, E, S, W]
# 0 = black, 1 = white

class State():
    def __init__(self, surf, connections):
        self.surf = surf
        self.connections = connections

bn = State(pygame.transform.scale(pygame.image.load('Circles/b_half.png'), (size, size)), [0, 1, 1, 1])
be = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_half.png'), (size, size)), 270), [1, 0, 1, 1])
bs = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_half.png'), (size, size)), 180), [1, 1, 0, 1])
bw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_half.png'), (size, size)), 90), [1, 1, 1, 0])
bns = State(pygame.transform.scale(pygame.image.load('Circles/b_i.png'), (size, size)), [0, 1, 0, 1])
bew = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_i.png'), (size, size)), 90), [1, 0, 1, 0])
bne = State(pygame.transform.scale(pygame.image.load('Circles/b_quarter.png'), (size, size)), [0, 0, 1, 1])
bes = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_quarter.png'), (size, size)), 270), [1, 0, 0, 1])
bsw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_quarter.png'), (size, size)), 180), [1, 1, 0, 0])
bwn = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/b_quarter.png'), (size, size)), 90), [0, 1, 1, 0])
b = State(pygame.transform.scale(pygame.image.load('Circles/b.png'), (size, size)), [0, 0, 0, 0])

wn = State(pygame.transform.scale(pygame.image.load('Circles/w_half.png'), (size, size)), [1, 0, 0, 0])
we = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_half.png'), (size, size)), 270), [0, 1, 0, 0])
ws = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_half.png'), (size, size)), 180), [0, 0, 1, 0])
ww = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_half.png'), (size, size)), 90), [0, 0, 0, 1])
wns = State(pygame.transform.scale(pygame.image.load('Circles/w_i.png'), (size, size)), [1, 0, 1, 0])
wew = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_i.png'), (size, size)), 90), [0, 1, 0, 1])
wne = State(pygame.transform.scale(pygame.image.load('Circles/w_quarter.png'), (size, size)), [1, 1, 0, 0])
wes = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_quarter.png'), (size, size)), 270), [0, 1, 1, 0])
wsw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_quarter.png'), (size, size)), 180), [0, 0, 1, 1])
wwn = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Circles/w_quarter.png'), (size, size)), 90), [1, 0, 0, 1])
w = State(pygame.transform.scale(pygame.image.load('Circles/w.png'), (size, size)), [1, 1, 1, 1])

tileSet = []

tileSet.append(bn)
tileSet.append(be)
tileSet.append(bs)
tileSet.append(bw)
tileSet.append(bns)
tileSet.append(bew)
tileSet.append(bne)
tileSet.append(bes)
tileSet.append(bsw)
tileSet.append(bwn)
tileSet.append(b)
tileSet.append(wn)
tileSet.append(we)
tileSet.append(ws)
tileSet.append(ww)
tileSet.append(wns)
tileSet.append(wew)
tileSet.append(wne)
tileSet.append(wes)
tileSet.append(wsw)
tileSet.append(wwn)
tileSet.append(w)

def wfcStep(board):
    newBoard = board.copy()
    # if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
    #     #print("finished")
    #     return board

    mini = random.randrange(0, len(board))
    minj = random.randrange(0, len(board[0]))
    minimum = len(board[mini][minj])
    while len(board[mini][minj]) == 1:
        mini = random.randrange(0, len(board))
        minj = random.randrange(0, len(board[0]))
        minimum = len(board[mini][minj])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(board[i][j]) == 1:
                continue
            if len(board[i][j]) < minimum:
                minimum = len(board[i][j])
                mini = i
                minj = j
    if minimum == 0:
        #print("imposible")
        return board
    
    newBoard[mini][minj] = [random.choice(board[mini][minj])]

    # north
    if minj > 0:
        if len(board[mini][minj - 1]) != 1:
            rem = []
            for k in board[mini][minj - 1]:
                if k.connections[2] != newBoard[mini][minj][0].connections[0]:
                    rem.append(k)
            for i in rem:
                newBoard[mini][minj - 1].remove(i)
    
    # west
    if mini > 0:
        if len(board[mini - 1][minj]) != 1:
            rem = []
            for k in board[mini - 1][minj]:
                if k.connections[1] != newBoard[mini][minj][0].connections[3]:
                    rem.append(k)
            for i in rem:
                newBoard[mini - 1][minj].remove(i)

    # south
    if minj < len(board[0]) - 1:
        if len(board[mini][minj + 1]) != 1:
            rem = []
            for k in board[mini][minj + 1]:
                if k.connections[0] != newBoard[mini][minj][0].connections[2]:
                    rem.append(k)
            for i in rem:
                newBoard[mini][minj + 1].remove(i)

    # east
    if mini < len(board) - 1:
        if len(board[mini + 1][minj]) != 1:
            rem = []
            for k in board[mini + 1][minj]:
                if k.connections[3] != newBoard[mini][minj][0].connections[1]:
                    rem.append(k)
            for i in rem:
                newBoard[mini + 1][minj].remove(i)
    
    return newBoard

def drawBoard(screen, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            possibleStates = len(board[i][j])
            if possibleStates == 1:
                board[i][j][0].surf.set_alpha(100)
                screen.blit(board[i][j][0].surf, (i*size, j*size))
            else:
                s = pygame.Surface((size, size))
                pygame.Surface.fill(s, pygame.Color(200, 200, 200))
                screen.blit(s,  (i*size, j*size))
                # for k in range(possibleStates):
                #     board[i][j][k].surf.set_alpha(100//possibleStates)
                #     screen.blit(board[i][j][k].surf, (i*size, j*size))

def main():
    run = True

    clock = pygame.time.Clock()

    board = [[tileSet.copy() for _ in range(HEIGHT//size)] for _ in range(WIDTH//size)]

    pause = False

    while run:
        pygame.display.set_caption("Wave Function Collapse Algorithm        || FPS: " + str(clock.get_fps()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                board = wfcStep(board)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = not pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[tileSet.copy() for _ in range(HEIGHT//size)] for _ in range(WIDTH//size)]

        screen.fill((50, 50, 50))
        if not pause:
            for _ in range(40):
                board = wfcStep(board)
        if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
            board = [[tileSet.copy() for _ in range(HEIGHT//size)] for _ in range(WIDTH//size)]
        drawBoard(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()