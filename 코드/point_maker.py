import numpy as np
import cv2
from const_data import *
from module import conv, num2coord
from section_maker import SECTION

HEIGHT = 32
WIDTH = 59

# 어떤 모델을 불러올지 결정
'''
key = input()
PREDICT = MODEL_DICT[key]
'''
PREDICT = SPRING_EVENING_SUNNY

# 모델이 생성한 결과를 그리드 배열판에 올림
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
map = np.zeros(shape=(HEIGHT, WIDTH))
idx = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            map[y][x] = PREDICT[idx]
            idx += 1

# 모델 생성 결과를 LPF로 뭉개줌
LPF = [[1/10, 1/10, 1/10],
       [1/10, 2/10, 1/10],
       [1/10, 1/10, 1/10]]
map = conv(map, np.array(LPF), padding=1)

# 그 중에서 범죄율이 높은 점들을 구역별로 추출
HOT_POINTS = [[], [], []]
for i in range(3):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
                continue

# A, B, C 알고리즘
res_A = np.zeros((HEIGHT, WIDTH))
res_B = np.zeros((HEIGHT, WIDTH))
res_C = np.zeros((HEIGHT, WIDTH))

# y, x는 중앙점
flag = 2
for x in range(2, WIDTH-2, 4):
    for y in range(2, HEIGHT-2, 4):
        if flag == 2:
            flag += 1
        else:
            flag = 2
        max_num = -1
        max_coord = [y, x]
        # 중앙점 기준 양 옆 2개씩 모아서 대소 비교
        for i in range(-2, 3):
            for j in range(-2, 3):
                a, b = x+i, y+j
                if img[b][a][0] != 255 or img[b][a][1] != 255 or img[b][a][2] != 255:
                    res_C[b][a] = flag
                if map[b][a] > max_num:
                    max_num = map[b][a]
                    max_coord = [b, a]
        # 그 중 최댓값이 d, c
        d, c = max_coord
        if img[d][c][0] == 255 and img[d][c][1] == 255 and img[d][c][2] == 255:
            res_C[d][c] = 0
        else:
            res_C[d][c] = 1

img_C = img
for x in range(WIDTH):
    for y in range(HEIGHT):
        if res_C[y][x] == 1:
            img_C[y][x][0] = 255
            img_C[y][x][1] = 10
            img_C[y][x][2] = 10
        elif res_C[y][x] == 2:
            img_C[y][x][0] = 200
            img_C[y][x][1] = 180
            img_C[y][x][2] = 200
        elif res_C[y][x] == 3:
            img_C[y][x][0] = 180
            img_C[y][x][1] = 200
            img_C[y][x][2] = 200
img_C = cv2.resize(img_C, dsize=(WIDTH*10, HEIGHT*10), interpolation=cv2.INTER_NEAREST_EXACT)

final = []
for i in range(3):
    tmp = []
    print(i)
    for c in SECTION[i]:
        y, x = c
        if res_C[y][x] == 1:
            tmp.append(c)
    final.append(tmp)

print(final)
