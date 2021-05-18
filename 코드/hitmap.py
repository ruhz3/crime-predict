
# ================================================
# hitmap.py
# - 예측한 결과를 지도 위에 히트맵으로 시각화
# ================================================

import numpy as np
import cv2
from const_data import *

CRIME_PREDICT = SPRING_EVENING_SUNNY

WIDTH = 59
HEIGHT = 32
GRID_NUM = 1107
'''
d = {
    7: [255, 0, 0],
    6: [255, 69, 0],
    5: [255, 140, 0],
    4: [255, 165, 0],
    3: [255, 215, 0],
    2: [255, 255, 0],
    1: [255, 255, 224],
    0: [255, 255, 240]
}

d = {
    7: [255, 0, 50],
    6: [255, 100, 60],
    5: [255, 120, 70],
    4: [255, 140, 80],
    3: [255, 160, 90],
    2: [255, 180, 100],
    1: [255, 200, 110],
    0: [255, 220, 120]
}
'''
d = {
    7: [255, 0, 50],
    6: [255, 255, 255],
    5: [255, 255, 255],    4: [255, 255, 255],    3: [255, 255, 255],    2: [255, 255, 255],
    1: [255, 255, 255],
    0: [255, 255, 255]}

# 그리드 이미지를 배열로 변환
grid = []
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            grid.append([y, x])


# 히스토그램을 통해 각 그리드의 색깔을 설정
grid_color = []
histogram = np.zeros(256, np.float_)
for i in range(GRID_NUM):
    histogram[CRIME_PREDICT[i]] += 1  # Make histogram!
for i in range(256):
    histogram[i] /= GRID_NUM  # Normalize it!
for i in range(1, 256):
    histogram[i] += histogram[i-1]  # Accumulate it!
for i in range(1, 256):
    histogram[i] = round(histogram[i] * 255)  # Convert to int(round)!
for i in CRIME_PREDICT:
    key = int(histogram[i] / 32)  # ....?
    grid_color.append(d[key])
for i in range(GRID_NUM):
    y, x = grid[i]
    result[y][x][0] = grid_color[i][2]
    result[y][x][1] = grid_color[i][1]
    result[y][x][2] = grid_color[i][0]


# 히트맵과 배경이될 지도를 사이즈 통일
result = cv2.resize(result, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
background = cv2.imread('img/map.png', 1)
background = cv2.resize(background, dsize=(WIDTH*20, HEIGHT*20))

# 키 입력이 있을 때 마다 0.2씩 더 강하게 블렌드
a = 0.0
while(a <= 1.0):
    b = 1.0 - a
    dst = cv2.addWeighted(result, a, background, b, 0)
    cv2.imshow('hitmap', dst)
    cv2.waitKey()
    a += 0.2




