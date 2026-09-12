import pygame
import random

# Falta arreglar algo, no sé el qué xd

pygame.init()

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

size = 15

# [N, E, S, W]
# 0 = www, 1 = wwb, 2 = wbw, 3 = wbb, 4 =  bww, 5 = bwb, 6 = bbw, 7 = bbb

class State():
    def __init__(self, surf, connections, symmetry):
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

bend = State(pygame.transform.scale(pygame.image.load('Rooms/bend.png'), (size, size)), [3, 6, 0, 0], "L")
corner = State(pygame.transform.scale(pygame.image.load('Rooms/corner.png'), (size, size)), [6, 3, 7, 7], "L")
corridor = State(pygame.transform.scale(pygame.image.load('Rooms/corridor.png'), (size, size)), [5, 7, 5, 7], "/")
door = State(pygame.transform.scale(pygame.image.load('Rooms/door.png'), (size, size)), [0, 3, 5, 3], "T")
empty = State(pygame.transform.scale(pygame.image.load('Rooms/empty.png'), (size, size)), [0, 0, 0, 0], "X")
side = State(pygame.transform.scale(pygame.image.load('Rooms/side.png'), (size, size)), [7, 6, 0, 6], "T")
t = State(pygame.transform.scale(pygame.image.load('Rooms/t.png'), (size, size)), [7, 5, 5, 5], "T")
turn = State(pygame.transform.scale(pygame.image.load('Rooms/turn.png'), (size, size)), [5, 5, 7, 7], "L")
wall = State(pygame.transform.scale(pygame.image.load('Rooms/wall.png'), (size, size)), [7, 7, 7, 7], "X")

tileSet = []

tileSet.extend(bend.createSymmetries())
tileSet.extend(corner.createSymmetries())
tileSet.extend(corridor.createSymmetries())
tileSet.extend(door.createSymmetries())
tileSet.extend(empty.createSymmetries())
tileSet.extend(side.createSymmetries())
tileSet.extend(t.createSymmetries())
tileSet.extend(turn.createSymmetries())
tileSet.extend(wall.createSymmetries())

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

    pause = True

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
                board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]

        screen.fill((50, 50, 50))
        
        if not pause:
            board = wfcStep(board)

        if all(all(len(board[i][j]) == 1 for j in range(len(board[0]))) for i in range(len(board))):
            board = [[tileSet.copy() for _ in range(WIDTH//size)] for _ in range(HEIGHT//size)]
        drawBoard(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()