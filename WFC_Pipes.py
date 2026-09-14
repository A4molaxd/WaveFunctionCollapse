import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

size = 100

# [N, E, S, W]
# 0 = empty, 1 = path

class State():
    def __init__(self, surf, connections):
        self.surf = surf
        self.connections = connections

cornerne = State(pygame.transform.scale(pygame.image.load('Knots\corner.png'), (size, size)), [1, 1, 0, 0])
cornerse = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots\corner.png'), (size, size)), 270), [0, 1, 1, 0])
cornersw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots\corner.png'), (size, size)), 180), [0, 0, 1, 1])
cornernw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots\corner.png'), (size, size)), 90), [1, 0, 0, 1])
crossu = State(pygame.transform.scale(pygame.image.load('Knots\cross.png'), (size, size)), [1, 1, 1, 1])
crossd = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots\cross.png'), (size, size)), 90), [1, 1, 1, 1])
empty = State(pygame.transform.scale(pygame.image.load('Knots\empty.png'), (size, size)), [0, 0, 0, 0])
lineew = State(pygame.transform.scale(pygame.image.load('Knots\line.png'), (size, size)), [0, 1, 0, 1])
linens = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots\line.png'), (size, size)), 90), [1, 0, 1, 0])
tn = State(pygame.transform.scale(pygame.image.load('Knots/t.png'), (size, size)), [0, 1, 1, 1])
te = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots/t.png'), (size, size)), 270), [1, 0, 1, 1])
ts = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots/t.png'), (size, size)), 180), [1, 1, 0, 1])
tw = State(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Knots/t.png'), (size, size)), 90), [1, 1, 1, 0])

tileSet = []

tileSet.append(cornerne)
tileSet.append(cornerse)
tileSet.append(cornersw)
tileSet.append(cornernw)
tileSet.append(crossu)
tileSet.append(crossd)
tileSet.append(empty)
tileSet.append(linens)
tileSet.append(lineew)
tileSet.append(tn)
tileSet.append(te)
tileSet.append(ts)
tileSet.append(tw)

def wfcStep(board):
    newBoard = board.copy()
    if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
        #print("finished")
        return board

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
                for k in range(possibleStates):
                    board[i][j][k].surf.set_alpha(100//possibleStates)
                    screen.blit(board[i][j][k].surf, (i*size, j*size))

def main():
    run = True

    clock = pygame.time.Clock()

    board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

    while run:
        pygame.display.set_caption("Wave Function Collapse Algorithm        || FPS: " + str(clock.get_fps()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ...
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

        screen.fill((50, 50, 50))
        for _ in range(1):
            board = wfcStep(board)
        if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
            board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
        drawBoard(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()