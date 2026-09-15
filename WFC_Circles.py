import WFC

# [N, E, S, W]
# 0 = black, 1 = white

b1 = WFC.State([0, 1, 1, 1], img = 'Circles/b_half.png')
b2 = WFC.State([0, 1, 0, 1], img = 'Circles/b_i.png')
b3 = WFC.State([0, 0, 1, 1], img = 'Circles/b_quarter.png')
b = WFC.State([0, 0, 0, 0], img = 'Circles/b.png')
w1 = WFC.State([1, 0, 0, 0], img = 'Circles/w_half.png')
w2 = WFC.State([1, 0, 1, 0], img = 'Circles/w_i.png')
w3 = WFC.State([1, 1, 0, 0], img = 'Circles/w_quarter.png')
w = WFC.State([1, 1, 1, 1], img = 'Circles/w.png')

tileSet = []

tileSet.extend(b1.createSymmetries("L"))
tileSet.extend(b2.createSymmetries("I"))
tileSet.extend(b3.createSymmetries("L"))
tileSet.append(b)
tileSet.extend(w1.createSymmetries("L"))
tileSet.extend(w2.createSymmetries("I"))
tileSet.extend(w3.createSymmetries("L"))
tileSet.append(w)

if __name__ == '__main__':
    WFC.main(tileSet)