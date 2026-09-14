import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

size = 40

DRAW_POSSIBLE = False

STEPS = 100

# [N, E, S, W]
# 0 = empty, 1 = path

#TODO: Change scale on this file (self.surf = pygame.transform.scale(...)), rather than on each separate image

class State():
    def __init__(self, surf, connections, symmetry = None):
        self.surf = surf
        self.connections = connections
        self.symmetry = symmetry
    
    def createSymmetries(self):
        l = [State(self.surf, self.connections, self.symmetry)]
        
        if self.symmetry == "X":
            pass
        elif self.symmetry == "L":
            l.append(State(pygame.transform.rotate(self.surf, 90),  [self.connections[1], self.connections[2], int("".join(list(bin(self.connections[3])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[0])[2:].zfill(3)[::-1])), 2)], self.symmetry))
            l.append(State(pygame.transform.rotate(self.surf, 180), [self.connections[2], self.connections[3], int("".join(list(bin(self.connections[0])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[1])[2:].zfill(3)[::-1])), 2)], self.symmetry))
            l.append(State(pygame.transform.rotate(self.surf, 270), [self.connections[3], self.connections[0], int("".join(list(bin(self.connections[1])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[2])[2:].zfill(3)[::-1])), 2)], self.symmetry))
        elif self.symmetry == "T": 
            l.append(State(pygame.transform.rotate(self.surf, 90),  [self.connections[1], self.connections[2], self.connections[3], self.connections[0]], self.symmetry))
            l.append(State(pygame.transform.rotate(self.surf, 180), [int("".join(list(bin(self.connections[2])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[3])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[0])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[1])[2:].zfill(3)[::-1])), 2)], self.symmetry))
            l.append(State(pygame.transform.rotate(self.surf, 270), [int("".join(list(bin(self.connections[3])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[0])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[1])[2:].zfill(3)[::-1])), 2), int("".join(list(bin(self.connections[2])[2:].zfill(3)[::-1])), 2)], self.symmetry))
        elif self.symmetry == "I":
            l.append(State(pygame.transform.rotate(self.surf, 90), self.connections, self.symmetry))
        elif self.symmetry == "/":
             l.append(State(pygame.transform.rotate(self.surf, 90), [self.connections[1], self.connections[2], self.connections[3], self.connections[0]], self.symmetry))
        return l

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

    return collapseCell(mini, minj, board, newBoard)

def collapseCell(i, j, board, newBoard):
    # north
    if j > 0:
        if len(board[i][j - 1]) > 1:
            rem = []
            for k in board[i][j - 1]:
                if k.connections[2] != newBoard[i][j][0].connections[0]:
                    rem.append(k)
            for it in rem:
                newBoard[i][j - 1].remove(it)
            if len(board[i][j - 1]) == 1:
                collapseCell(i, j - 1, board, newBoard)
    
    # west
    if i > 0:
        if len(board[i - 1][j]) > 1:
            rem = []
            for k in board[i - 1][j]:
                if k.connections[1] != newBoard[i][j][0].connections[3]:
                    rem.append(k)
            for it in rem:
                newBoard[i - 1][j].remove(it)
            if len(board[i - 1][j]) == 1:
                collapseCell(i - 1, j, board, newBoard)

    # south
    if j < len(board[0]) - 1:
        if len(board[i][j + 1]) > 1:
            rem = []
            for k in board[i][j + 1]:
                if k.connections[0] != newBoard[i][j][0].connections[2]:
                    rem.append(k)
            for it in rem:
                newBoard[i][j + 1].remove(it)
            if len(board[i][j + 1]) == 1:
                collapseCell(i, j + 1, board, newBoard)

    # east
    if i < len(board) - 1:
        if len(board[i + 1][j]) > 1:
            rem = []
            for k in board[i + 1][j]:
                if k.connections[3] != newBoard[i][j][0].connections[1]:
                    rem.append(k)
            for it in rem:
                newBoard[i + 1][j].remove(it)
            if len(board[i + 1][j]) == 1:
                collapseCell(i + 1, j, board, newBoard)
    
    return True, newBoard

def drawBoard(screen, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            possibleStates = len(board[i][j])
            if possibleStates == 1:
                board[i][j][0].surf.set_alpha(100)
                screen.blit(board[i][j][0].surf, (i*size, j*size))
            else:
                if DRAW_POSSIBLE:
                    for k in range(possibleStates):
                        board[i][j][k].surf.set_alpha(100//possibleStates)
                        screen.blit(board[i][j][k].surf, (i*size, j*size))
                else:
                    s = pygame.Surface((size, size))
                    s.fill(pygame.Color(100, 100, 100))
                    screen.blit(s, (i*size, j*size))
def main(tileSet):
    run = True

    clock = pygame.time.Clock()

    board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

    pause = False

    finished = False

    while run:
        pygame.display.set_caption("Wave Function Collapse Algorithm        || FPS: " + str(clock.get_fps()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                finished = False
                board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                possible, board = wfcStep(board)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = not pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

        screen.fill((50, 50, 50))
        if not pause and not finished:
            for _ in range(STEPS):
                possible, board = wfcStep(board)
                if not possible:
                    board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
        if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
            finished = True
        drawBoard(screen, board)
        pygame.display.flip()
        
        clock.tick(60)