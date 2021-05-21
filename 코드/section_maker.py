# ================================================
# section_maker.py
# - 구역 별로 좌표를 분할한 배열 생성
# ================================================

import cv2
import numpy as np
from module import num2coord, coord2num

WIDTH = 59
HEIGHT = 32
'''
<COLOR_DICT 생성>
img = cv2.imread("222.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
grids = []

for x in range(WIDTH):
    for y in range(HEIGHT):
        grids.append(img[y][x])

new_list = []
for i in grids:
    alreadyIn = False
    for j in new_list:
        if np.array_equal(i, j):
            alreadyIn = True
    if alreadyIn is False:
        new_list.append(i)
print(new_list)
'''
COLOR_DICT = {0: [0, 0, 0],
              1: [36,  28, 237],
              2: [127, 127, 127],
              3: [21,   0, 136],
              4: [39, 127, 255],
              5: [76, 177,  34],
              6: [0, 242, 255],
              7: [232, 162,   0],
              8: [204,  72,  63],
              9: [176, 228, 239],
              10: [164,  73, 163],
              11: [14, 201, 255],
              12: [201, 174, 255],
              13: [87, 122, 185],
              14: [195, 195, 195]}
'''
<DONG_DICT 생성>
img = np.zeros(shape=(15, 1, 3), dtype=np.uint8)
for i in range(15):
    img[i] = COLOR_DICT[i]

result = cv2.resize(dsize=(150, 150), src=img, interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('r', result)
cv2.waitKey()
'''
DONG_DICT = {
    0: '중림동', 1: '소공동', 2: '회현동', 3: '명동',  4: '필동', 5: '을지로동',
    6: '장충동', 7: '광희동', 8: '다산동', 9: '약수동', 10: '신당동', 11: '청구동',
    12: '동화동', 13: '신당5동', 14: '황학동'
}

# 그리드 이미지를 배열로 변환
img = cv2.imread("img/dong.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
grids = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            grids.append([y, x])

# 그리드를 동별로 분리
grids_dong = []
for i in range(15):
    new = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if img[y][x][0] == COLOR_DICT[i][0] and img[y][x][1] == COLOR_DICT[i][1] and img[y][x][2] == COLOR_DICT[i][2]:
                new.append([y, x])
    grids_dong.append(new)

# 동을 구역별로 분류
SECTION = []
tmp = []
for i in range(0, 15):
    for j in grids_dong[i]:
        tmp.append(j)
    if i == 3 or i == 8 or i == 14:
        tmp.sort()
        SECTION.append(tmp)
        tmp = []

if __name__ == "__main__":
    for i in SECTION:
        print(i)

'''
<경찰서 위치 시각화>
pachool = [174, 963, 467, 711, 429, 185, 311, 161, 115, 50, 231]
jigoo = [919, 909, 679]
seo = [406, 152]
for i in range(len(pachool)):
    y, x = grids[pachool[i]]
    img[y][x][0] = 255
    img[y][x][1] = 0
    img[y][x][2] = 0
for i in range(len(jigoo)):
    y, x = grids[jigoo[i]]
    img[y][x][0] = 0
    img[y][x][1] = 255
    img[y][x][2] = 0
for i in range(len(seo)):
    y, x = grids[seo[i]]
    img[y][x][0] = 0
    img[y][x][1] = 0
    img[y][x][2] = 255

img = cv2.resize(img, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('hey', img)
cv2.waitKey()
'''