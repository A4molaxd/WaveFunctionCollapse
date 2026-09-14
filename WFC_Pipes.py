import WFC

# [N, E, S, W]
# 0 = empty, 1 = path

cornerne = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/corner.png'), (WFC.size, WFC.size)), [1, 1, 0, 0])
cornerse = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/corner.png'), (WFC.size, WFC.size)), 270), [0, 1, 1, 0])
cornersw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/corner.png'), (WFC.size, WFC.size)), 180), [0, 0, 1, 1])
cornernw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/corner.png'), (WFC.size, WFC.size)), 90), [1, 0, 0, 1])

crossu = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/cross.png'), (WFC.size, WFC.size)), [1, 1, 1, 1])
crossd = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/cross.png'), (WFC.size, WFC.size)), 90), [1, 1, 1, 1])

empty = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/empty.png'), (WFC.size, WFC.size)), [0, 0, 0, 0])

lineew = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/line.png'), (WFC.size, WFC.size)), [0, 1, 0, 1])
linens = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/line.png'), (WFC.size, WFC.size)), 90), [1, 0, 1, 0])

tn = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/t.png'), (WFC.size, WFC.size)), [0, 1, 1, 1])
te = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/t.png'), (WFC.size, WFC.size)), 270), [1, 0, 1, 1])
ts = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/t.png'), (WFC.size, WFC.size)), 180), [1, 1, 0, 1])
tw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Knots/t.png'), (WFC.size, WFC.size)), 90), [1, 1, 1, 0])

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

if __name__ == '__main__':
    WFC.main(tileSet)