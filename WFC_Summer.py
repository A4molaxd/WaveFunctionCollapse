import WFC

# [N, E, S, W]
# 0 = cliff se, 1 = grass, 2 = road, 3 = water, 4 = waterside ne, 5 = cliff nw, 6 = waterside sw, 7 = road ne, 8 = road sw

cliff0 = WFC.State([1, 0, 1, 0], img = 'Summer/cliff 0.png')
cliff1 = WFC.State([0, 1, 0, 1], img = 'Summer/cliff 1.png')
cliff2 = WFC.State([1, 5, 1, 5], img = 'Summer/cliff 2.png')
cliff3 = WFC.State([5, 1, 5, 1], img = 'Summer/cliff 3.png')

cliffcorner0 = WFC.State([0, 5, 1, 1], img = 'Summer/cliffcorner 0.png')
cliffcorner1 = WFC.State([5, 1, 1, 5], img = 'Summer/cliffcorner 1.png')
cliffcorner2 = WFC.State([1, 1, 5, 0], img = 'Summer/cliffcorner 2.png')
cliffcorner3 = WFC.State([1, 0, 0, 1], img = 'Summer/cliffcorner 3.png')

cliffturn0 = WFC.State([5, 0, 1, 1], img = 'Summer/cliffturn 0.png')
cliffturn1 = WFC.State([0, 1, 1, 0], img = 'Summer/cliffturn 1.png')
cliffturn2 = WFC.State([1, 1, 0, 5], img = 'Summer/cliffturn 2.png')
cliffturn3 = WFC.State([1, 5, 5, 1], img = 'Summer/cliffturn 3.png')

grass0 = WFC.State([1, 1, 1, 1], img = 'Summer/grass 0.png')

grasscorner0 = WFC.State([7, 7, 2, 2], img = 'Summer/grasscorner 0.png')
grasscorner1 = WFC.State([8, 2, 2, 7], img = 'Summer/grasscorner 1.png')
grasscorner2 = WFC.State([2, 2, 8, 8], img = 'Summer/grasscorner 2.png')
grasscorner3 = WFC.State([2, 8, 7, 2], img = 'Summer/grasscorner 3.png')

road0 = WFC.State([2, 8, 1, 8], img = 'Summer/road 0.png')
road1 = WFC.State([7, 1, 7, 2], img = 'Summer/road 1.png')
road2 = WFC.State([1, 7, 2, 7], img = 'Summer/road 2.png')
road3 = WFC.State([8, 2, 8, 1], img = 'Summer/road 3.png')

roadturn0 = WFC.State([8, 8, 1, 1], img = 'Summer/roadturn 0.png')
roadturn1 = WFC.State([7, 1, 1, 8], img = 'Summer/roadturn 1.png')
roadturn2 = WFC.State([1, 1, 7, 7], img = 'Summer/roadturn 2.png')
roadturn3 = WFC.State([1, 7, 8, 1], img = 'Summer/roadturn 3.png')

water0 = WFC.State([3, 3, 3, 3], img = 'Summer/water_a 0.png')
water1 = WFC.State([3, 3, 3, 3], img = 'Summer/water_b 0.png')
water2 = WFC.State([3, 3, 3, 3], img = 'Summer/water_c 0.png')

watercorner0 = WFC.State([4, 4, 1, 1], img = 'Summer/watercorner 0.png')
watercorner1 = WFC.State([6, 1, 1, 4], img = 'Summer/watercorner 1.png')
watercorner2 = WFC.State([1, 1, 6, 6], img = 'Summer/watercorner 2.png')
watercorner3 = WFC.State([1, 6, 4, 1], img = 'Summer/watercorner 3.png')

waterside0 = WFC.State([3, 4, 1, 4], img = 'Summer/waterside 0.png')
waterside1 = WFC.State([6, 1, 6, 3], img = 'Summer/waterside 1.png')
waterside2 = WFC.State([1, 6, 3, 6], img = 'Summer/waterside 2.png')
waterside3 = WFC.State([4, 3, 4, 1], img = 'Summer/waterside 3.png')

waterturn0 = WFC.State([3, 3, 4, 4], img = 'Summer/waterturn 0.png')
waterturn1 = WFC.State([3, 4, 6, 3], img = 'Summer/waterturn 1.png')
waterturn2 = WFC.State([6, 6, 3, 3], img = 'Summer/waterturn 2.png')
waterturn3 = WFC.State([4, 3, 3, 6], img = 'Summer/waterturn 3.png')

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