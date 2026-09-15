import WFC

# [N, E, S, W]
# 0 = www, 1 = wwb, 2 = wbw, 3 = wbb, 4 =  bww, 5 = bwb, 6 = bbw, 7 = bbb

bend = WFC.State([3, 6, 0, 0], img = 'Rooms/bend.png')
corner = WFC.State([6, 3, 7, 7], img = 'Rooms/corner.png')
corridor = WFC.State([5, 7, 5, 7], img = 'Rooms/corridor.png')
door = WFC.State([0, 3, 5, 3], img = 'Rooms/door.png')
empty = WFC.State([0, 0, 0, 0], img = 'Rooms/empty.png')
side = WFC.State([7, 6, 0, 6], img = 'Rooms/side.png',)
t = WFC.State([7, 5, 5, 5], img = 'Rooms/t.png')
turn = WFC.State([5, 5, 7, 7], img = 'Rooms/turn.png')
wall = WFC.State([7, 7, 7, 7], img = 'Rooms/wall.png')

tileSet = []

tileSet.extend(bend.createSymmetries("L", symmetryMode = 3))
tileSet.extend(corner.createSymmetries("L", symmetryMode = 3))
tileSet.extend(corridor.createSymmetries("/", symmetryMode = 3))
tileSet.extend(door.createSymmetries("T", symmetryMode = 3))
tileSet.extend(empty.createSymmetries("X", symmetryMode = 3))
tileSet.extend(side.createSymmetries("T", symmetryMode = 3))
tileSet.extend(t.createSymmetries("T", symmetryMode = 3))
tileSet.extend(turn.createSymmetries("L", symmetryMode = 3))
tileSet.extend(wall.createSymmetries("X", symmetryMode = 3))


if __name__ == '__main__':
    WFC.main(tileSet)