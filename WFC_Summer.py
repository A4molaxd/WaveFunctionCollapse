import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

size = 100

# [N, E, S, W]
# c = cliff, g = grass, r = road, w = water
# 0 = clifff, 1 = grass, 2 = road, 3 = water, 4 = waterside, 5 = cliffb

class State():
    def __init__(self, surf, connections):
        self.surf = surf
        self.connections = connections

cliff0 = State(pygame.transform.scale(pygame.image.load('Summer/cliff 0.png'), (size, size)), [1, 0, 1, 0])
cliff1 = State(pygame.transform.scale(pygame.image.load('Summer/cliff 1.png'), (size, size)), [0, 1, 0, 1])
cliff2 = State(pygame.transform.scale(pygame.image.load('Summer/cliff 2.png'), (size, size)), [1, 5, 1, 5])
cliff3 = State(pygame.transform.scale(pygame.image.load('Summer/cliff 3.png'), (size, size)), [5, 1, 5, 1])
cliffcorner0 = State(pygame.transform.scale(pygame.image.load('Summer/cliffcorner 0.png'), (size, size)), [0, 5, 1, 1])
cliffcorner1 = State(pygame.transform.scale(pygame.image.load('Summer/cliffcorner 1.png'), (size, size)), [5, 1, 1, 5])
cliffcorner2 = State(pygame.transform.scale(pygame.image.load('Summer/cliffcorner 2.png'), (size, size)), [1, 1, 5, 0])
cliffcorner3 = State(pygame.transform.scale(pygame.image.load('Summer/cliffcorner 3.png'), (size, size)), [1, 0, 0, 1])
cliffturn0 = State(pygame.transform.scale(pygame.image.load('Summer/cliffturn 0.png'), (size, size)), [0, 0, 1, 1])
cliffturn1 = State(pygame.transform.scale(pygame.image.load('Summer/cliffturn 1.png'), (size, size)), [0, 1, 1, 0])
cliffturn2 = State(pygame.transform.scale(pygame.image.load('Summer/cliffturn 2.png'), (size, size)), [1, 1, 0, 5])
cliffturn3 = State(pygame.transform.scale(pygame.image.load('Summer/cliffturn 3.png'), (size, size)), [1, 5, 5, 1])
grass0 = State(pygame.transform.scale(pygame.image.load('Summer/grass 0.png'), (size, size)), [1, 1, 1, 1])
grasscorner0 = State(pygame.transform.scale(pygame.image.load('Summer/grasscorner 0.png'), (size, size)), [2, 2, 2, 2])
grasscorner1 = State(pygame.transform.scale(pygame.image.load('Summer/grasscorner 1.png'), (size, size)), [2, 2, 2, 2])
grasscorner2 = State(pygame.transform.scale(pygame.image.load('Summer/grasscorner 2.png'), (size, size)), [2, 2, 2, 2])
grasscorner3 = State(pygame.transform.scale(pygame.image.load('Summer/grasscorner 3.png'), (size, size)), [2, 2, 2, 2])
road0 = State(pygame.transform.scale(pygame.image.load('Summer/road 0.png'), (size, size)), [2, 2, 1, 2])
road1 = State(pygame.transform.scale(pygame.image.load('Summer/road 1.png'), (size, size)), [2, 1, 2, 2])
road2 = State(pygame.transform.scale(pygame.image.load('Summer/road 2.png'), (size, size)), [1, 2, 2, 2])
road3 = State(pygame.transform.scale(pygame.image.load('Summer/road 3.png'), (size, size)), [2, 2, 2, 1])
roadturn0 = State(pygame.transform.scale(pygame.image.load('Summer/roadturn 0.png'), (size, size)), [2, 2, 1, 1])
roadturn1 = State(pygame.transform.scale(pygame.image.load('Summer/roadturn 1.png'), (size, size)), [2, 1, 1, 2])
roadturn2 = State(pygame.transform.scale(pygame.image.load('Summer/roadturn 2.png'), (size, size)), [1, 1, 2, 2])
roadturn3 = State(pygame.transform.scale(pygame.image.load('Summer/roadturn 3.png'), (size, size)), [1, 2, 2, 1])
water0 = State(pygame.transform.scale(pygame.image.load('Summer/water_a 0.png'), (size, size)), [3, 3, 3, 3])
water1 = State(pygame.transform.scale(pygame.image.load('Summer/water_b 0.png'), (size, size)), [3, 3, 3, 3])
water2 = State(pygame.transform.scale(pygame.image.load('Summer/water_c 0.png'), (size, size)), [3, 3, 3, 3])
watercorner0 = State(pygame.transform.scale(pygame.image.load('Summer/watercorner 0.png'), (size, size)), [4, 4, 1, 1])
watercorner1 = State(pygame.transform.scale(pygame.image.load('Summer/watercorner 1.png'), (size, size)), [4, 1, 1, 4])
watercorner2 = State(pygame.transform.scale(pygame.image.load('Summer/watercorner 2.png'), (size, size)), [1, 1, 4, 4])
watercorner3 = State(pygame.transform.scale(pygame.image.load('Summer/watercorner 3.png'), (size, size)), [1, 4, 4, 1])
waterside0 = State(pygame.transform.scale(pygame.image.load('Summer/waterside 0.png'), (size, size)), [3, 4, 1, 4])
waterside1 = State(pygame.transform.scale(pygame.image.load('Summer/waterside 1.png'), (size, size)), [4, 1, 4, 3])
waterside2 = State(pygame.transform.scale(pygame.image.load('Summer/waterside 2.png'), (size, size)), [1, 4, 3, 4])
waterside3 = State(pygame.transform.scale(pygame.image.load('Summer/waterside 3.png'), (size, size)), [4, 3, 4, 1])
waterturn0 = State(pygame.transform.scale(pygame.image.load('Summer/waterturn 0.png'), (size, size)), [3, 3, 4, 4])
waterturn1 = State(pygame.transform.scale(pygame.image.load('Summer/waterturn 1.png'), (size, size)), [3, 4, 4, 3])
waterturn2 = State(pygame.transform.scale(pygame.image.load('Summer/waterturn 2.png'), (size, size)), [4, 4, 3, 3])
waterturn3 = State(pygame.transform.scale(pygame.image.load('Summer/waterturn 3.png'), (size, size)), [4, 3, 3, 4])

tileSet = []

tileSet.append(cliff0)
tileSet.append(cliff1)
tileSet.append(cliff2)
tileSet.append(cliff3)
tileSet.append(cliffcorner0)
tileSet.append(cliffcorner1)
tileSet.append(cliffcorner2)
tileSet.append(cliffcorner3)
tileSet.append(cliffturn0)
tileSet.append(cliffturn1)
tileSet.append(cliffturn2)
tileSet.append(cliffturn3)
tileSet.append(grass0)
tileSet.append(grasscorner0)
tileSet.append(grasscorner1)
tileSet.append(grasscorner2)
tileSet.append(grasscorner3)
tileSet.append(road0)
tileSet.append(road1)
tileSet.append(road2)
tileSet.append(road3)
tileSet.append(roadturn0)
tileSet.append(roadturn1)
tileSet.append(roadturn2)
tileSet.append(roadturn3)
tileSet.append(water0)
tileSet.append(water1)
tileSet.append(water2)
tileSet.append(watercorner0)
tileSet.append(watercorner1)
tileSet.append(watercorner2)
tileSet.append(watercorner3)
tileSet.append(waterside0)
tileSet.append(waterside1)
tileSet.append(waterside2)
tileSet.append(waterside3)
tileSet.append(waterturn0)
tileSet.append(waterturn1)
tileSet.append(waterturn2)
tileSet.append(waterturn3)

def wfcStep(board):
    newBoard = board.copy()
    if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
        #print("finished")
        return True, board

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
        return False, board
    
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
    
    return True, newBoard

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

    pause = False

    while run:
        pygame.display.set_caption("Wave Function Collapse Algorithm        || FPS: " + str(clock.get_fps()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                possible, board = wfcStep(board)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = not pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

        screen.fill((50, 50, 50))
        if not pause:
            for _ in range(1):
                possible, board = wfcStep(board)
                if not possible:
                    board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
        if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
            board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
        drawBoard(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()