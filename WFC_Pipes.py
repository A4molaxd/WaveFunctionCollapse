import WFC

# [N, E, S, W]
# 0 = empty, 1 = path

corners = WFC.State([1, 1, 0, 0], 'Knots/corner.png')
crosses = WFC.State([1, 1, 1, 1], 'Knots/cross.png')
empty = WFC.State([0, 0, 0, 0], 'Knots/empty.png')
lines = WFC.State([0, 1, 0, 1], 'Knots/line.png')
ts = WFC.State([0, 1, 1, 1], 'Knots/t.png')

tileSet = []

tileSet.extend(corners.createSymmetries("L"))
tileSet.extend(crosses.createSymmetries("I"))
tileSet.append(empty)
tileSet.extend(lines.createSymmetries("I"))
tileSet.extend(ts.createSymmetries("L"))

if __name__ == '__main__':
    WFC.main(tileSet)