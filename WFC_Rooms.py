import WFC

# [N, E, S, W]
# 0 = www, 1 = wwb, 2 = wbw, 3 = wbb, 4 =  bww, 5 = bwb, 6 = bbw, 7 = bbb

bend = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/bend.png'), (WFC.size, WFC.size)), [3, 6, 0, 0], "L")
corner = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/corner.png'), (WFC.size, WFC.size)), [6, 3, 7, 7], "L")
corridor = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/corridor.png'), (WFC.size, WFC.size)), [5, 7, 5, 7], "/")
door = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/door.png'), (WFC.size, WFC.size)), [0, 3, 5, 3], "T")
empty = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/empty.png'), (WFC.size, WFC.size)), [0, 0, 0, 0], "X")
side = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/side.png'), (WFC.size, WFC.size)), [7, 6, 0, 6], "T")
t = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/t.png'), (WFC.size, WFC.size)), [7, 5, 5, 5], "T")
turn = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/turn.png'), (WFC.size, WFC.size)), [5, 5, 7, 7], "L")
wall = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Rooms/wall.png'), (WFC.size, WFC.size)), [7, 7, 7, 7], "X")

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


if __name__ == '__main__':
    WFC.main(tileSet)