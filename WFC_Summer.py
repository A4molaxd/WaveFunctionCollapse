import WFC

# [N, E, S, W]
# 0 = cliff se, 1 = grass, 2 = road, 3 = water, 4 = waterside ne, 5 = cliff nw, 6 = waterside sw, 7 = road ne, 8 = road sw

cliff0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliff 0.png'), (WFC.size, WFC.size)), [1, 0, 1, 0])
cliff1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliff 1.png'), (WFC.size, WFC.size)), [0, 1, 0, 1])
cliff2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliff 2.png'), (WFC.size, WFC.size)), [1, 5, 1, 5])
cliff3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliff 3.png'), (WFC.size, WFC.size)), [5, 1, 5, 1])

cliffcorner0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffcorner 0.png'), (WFC.size, WFC.size)), [0, 5, 1, 1])
cliffcorner1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffcorner 1.png'), (WFC.size, WFC.size)), [5, 1, 1, 5])
cliffcorner2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffcorner 2.png'), (WFC.size, WFC.size)), [1, 1, 5, 0])
cliffcorner3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffcorner 3.png'), (WFC.size, WFC.size)), [1, 0, 0, 1])

cliffturn0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffturn 0.png'), (WFC.size, WFC.size)), [5, 0, 1, 1])
cliffturn1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffturn 1.png'), (WFC.size, WFC.size)), [0, 1, 1, 0])
cliffturn2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffturn 2.png'), (WFC.size, WFC.size)), [1, 1, 0, 5])
cliffturn3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/cliffturn 3.png'), (WFC.size, WFC.size)), [1, 5, 5, 1])

grass0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/grass 0.png'), (WFC.size, WFC.size)), [1, 1, 1, 1])

grasscorner0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/grasscorner 0.png'), (WFC.size, WFC.size)), [7, 7, 2, 2])
grasscorner1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/grasscorner 1.png'), (WFC.size, WFC.size)), [8, 2, 2, 7])
grasscorner2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/grasscorner 2.png'), (WFC.size, WFC.size)), [2, 2, 8, 8])
grasscorner3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/grasscorner 3.png'), (WFC.size, WFC.size)), [2, 8, 7, 2])

road0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/road 0.png'), (WFC.size, WFC.size)), [2, 8, 1, 8])
road1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/road 1.png'), (WFC.size, WFC.size)), [7, 1, 7, 2])
road2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/road 2.png'), (WFC.size, WFC.size)), [1, 7, 2, 7])
road3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/road 3.png'), (WFC.size, WFC.size)), [8, 2, 8, 1])

roadturn0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/roadturn 0.png'), (WFC.size, WFC.size)), [8, 8, 1, 1])
roadturn1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/roadturn 1.png'), (WFC.size, WFC.size)), [7, 1, 1, 8])
roadturn2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/roadturn 2.png'), (WFC.size, WFC.size)), [1, 1, 7, 7])
roadturn3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/roadturn 3.png'), (WFC.size, WFC.size)), [1, 7, 8, 1])

water0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/water_a 0.png'), (WFC.size, WFC.size)), [3, 3, 3, 3])
water1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/water_b 0.png'), (WFC.size, WFC.size)), [3, 3, 3, 3])
water2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/water_c 0.png'), (WFC.size, WFC.size)), [3, 3, 3, 3])

watercorner0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/watercorner 0.png'), (WFC.size, WFC.size)), [4, 4, 1, 1])
watercorner1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/watercorner 1.png'), (WFC.size, WFC.size)), [6, 1, 1, 4])
watercorner2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/watercorner 2.png'), (WFC.size, WFC.size)), [1, 1, 6, 6])
watercorner3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/watercorner 3.png'), (WFC.size, WFC.size)), [1, 6, 4, 1])

waterside0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterside 0.png'), (WFC.size, WFC.size)), [3, 4, 1, 4])
waterside1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterside 1.png'), (WFC.size, WFC.size)), [6, 1, 6, 3])
waterside2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterside 2.png'), (WFC.size, WFC.size)), [1, 6, 3, 6])
waterside3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterside 3.png'), (WFC.size, WFC.size)), [4, 3, 4, 1])

waterturn0 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterturn 0.png'), (WFC.size, WFC.size)), [3, 3, 4, 4])
waterturn1 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterturn 1.png'), (WFC.size, WFC.size)), [3, 4, 6, 3])
waterturn2 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterturn 2.png'), (WFC.size, WFC.size)), [6, 6, 3, 3])
waterturn3 = WFC.State(WFC.pygame.transform.scale(WFC.pygame.image.load('Summer/waterturn 3.png'), (WFC.size, WFC.size)), [4, 3, 3, 6])

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

if __name__ == '__main__':
    WFC.main(tileSet)