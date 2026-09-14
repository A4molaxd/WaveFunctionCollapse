import WFC

# [N, E, S, W]
# 0 = black, 1 = white

bn = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_half.png'), (WFC.size, WFC.size)), [0, 1, 1, 1])
be = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_half.png'), (WFC.size, WFC.size)), 270), [1, 0, 1, 1])
bs = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_half.png'), (WFC.size, WFC.size)), 180), [1, 1, 0, 1])
bw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_half.png'), (WFC.size, WFC.size)), 90), [1, 1, 1, 0])

bns = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_i.png'), (WFC.size, WFC.size)), [0, 1, 0, 1])
bew = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_i.png'), (WFC.size, WFC.size)), 90), [1, 0, 1, 0])

bne = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_quarter.png'), (WFC.size, WFC.size)), [0, 0, 1, 1])
bes = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_quarter.png'), (WFC.size, WFC.size)), 270), [1, 0, 0, 1])
bsw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_quarter.png'), (WFC.size, WFC.size)), 180), [1, 1, 0, 0])
bwn = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b_quarter.png'), (WFC.size, WFC.size)), 90), [0, 1, 1, 0])

b = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/b.png'), (WFC.size, WFC.size)), [0, 0, 0, 0])

wn = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_half.png'), (WFC.size, WFC.size)), [1, 0, 0, 0])
we = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_half.png'), (WFC.size, WFC.size)), 270), [0, 1, 0, 0])
ws = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_half.png'), (WFC.size, WFC.size)), 180), [0, 0, 1, 0])
ww = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_half.png'), (WFC.size, WFC.size)), 90), [0, 0, 0, 1])

wns = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_i.png'), (WFC.size, WFC.size)), [1, 0, 1, 0])
wew = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_i.png'), (WFC.size, WFC.size)), 90), [0, 1, 0, 1])

wne = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_quarter.png'), (WFC.size, WFC.size)), [1, 1, 0, 0])
wes = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_quarter.png'), (WFC.size, WFC.size)), 270), [0, 1, 1, 0])
wsw = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_quarter.png'), (WFC.size, WFC.size)), 180), [0, 0, 1, 1])
wwn = WFC.State(WFC.pygame.transform.rotate(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w_quarter.png'), (WFC.size, WFC.size)), 90), [1, 0, 0, 1])

w = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Circles/w.png'), (WFC.size, WFC.size)), [1, 1, 1, 1])

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

if __name__ == '__main__':
    WFC.main(tileSet)