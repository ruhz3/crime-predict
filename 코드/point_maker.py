# ================================================
# point_maker.py
# - 구역별/알고리즘별 경유지 list 생성
# ================================================

import numpy as np
import cv2
import copy
from const_data import *
from module import conv, num2coord, coord2num
from section_maker import SECTION
from hitmap import *
import random

HEIGHT = 32
WIDTH = 59

COLOR_DICT = {
    -1: [255, 255, 255],
    0: [200, 180, 200],
    1: [180, 200, 200],
    2: [10, 10, 255]
}

# 어떤 모델을 불러올지 결정
'''
key = input()
PREDICT = MODEL_DICT[key]
'''


# 모델이 생성한 결과를 그리드 배열판에 올림
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
map = np.zeros(shape=(HEIGHT, WIDTH))

def extract_points(model_key, algorithm):
    print("making point...")
    global img, map
    PREDICT = MODEL_DICT[model_key]
    idx = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if not np.array_equal(img[y][x], np.array([255, 255, 255])):
                map[y][x] = PREDICT[idx] * 10
                idx += 1

    # 모델 생성 결과를 LPF로 뭉개줌
    LPF = [[1 / 10, 1 / 10, 1 / 10],
           [1 / 10, 2 / 10, 1 / 10],
           [1 / 10, 1 / 10, 1 / 10]]
    map = conv(map, np.array(LPF), padding=1)
    # view(image=hitmap_image(map=map), times=10, winname='map')
    # A, B, C 알고리즘
    res_A = np.full((HEIGHT, WIDTH), -1)
    res_B = np.full((HEIGHT, WIDTH), -1)
    res_C = np.full((HEIGHT, WIDTH), -1)

    # A, C 알고리즘은 체스판 모양으로 구역 시각화
    chess_switch = 0
    for x in range(2, WIDTH, 5):
        chess_switch = (chess_switch + 1) % 2
        for y in range(2, HEIGHT, 5):
            chess_switch = (chess_switch + 1) % 2
            # [y, x] 중앙점 기준 양옆 두개를 포함
            max_num = -1
            max_coord = [y, x]
            for i in range(-2, 3):
                for j in range(-2, 3):
                    b, a = y + j, x + i
                    if b < 0 or b >= HEIGHT or a < 0 or a >= WIDTH:
                        continue
                    if not np.array_equal(img[b][a], np.array([255, 255, 255])):
                        res_A[b][a] = chess_switch
                        res_B[b][a] = 0
                        res_C[b][a] = chess_switch
                    if map[b][a] > max_num:
                        max_num = map[b][a]
                        max_coord = [b, a]
            # A는 중앙점을 그대로 사용, C는 최대점 [d, c]를 사용
            if not np.array_equal(img[y][x], np.array([255, 255, 255])):
                res_A[y][x] = 2
            d, c = max_coord
            if not np.array_equal(img[d][c], np.array([255, 255, 255])):
                res_C[d][c] = 2

    # B 알고리즘은 threshold!
    THRESHOLD = 230
    for i in range(3):
        histogram = np.zeros(256, np.float_)
        for j in SECTION[i]:
            y, x = j
            histogram[int(map[y][x])] += 1  # Make Histogram!
        for j in range(256):
            histogram[j] /= len(SECTION[i])  # Normalize it!
        for j in range(1, 256):
            histogram[j] += histogram[j - 1]  # Accumulate it!
        for j in range(1, 256):
            histogram[j] = round(histogram[j] * 255)  # Convert to int(round)!
        for j in SECTION[i]:
            y, x = j
            key = int(histogram[int(map[y][x])])  # 0 to 255
            if THRESHOLD <= key <= 255:
                res_B[y][x] = 2

    # 나온 결과를 표현할 이미지 배열 생성
    img_A = copy.deepcopy(img)
    img_B = copy.deepcopy(img)
    img_C = copy.deepcopy(img)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            img_A[y][x] = COLOR_DICT[res_A[y][x]]
            img_B[y][x] = COLOR_DICT[res_B[y][x]]
            img_C[y][x] = COLOR_DICT[res_C[y][x]]
    img_A = cv2.resize(img_A, dsize=(WIDTH * 10, HEIGHT * 10), interpolation=cv2.INTER_NEAREST_EXACT)
    img_B = cv2.resize(img_B, dsize=(WIDTH * 10, HEIGHT * 10), interpolation=cv2.INTER_NEAREST_EXACT)
    img_C = cv2.resize(img_C, dsize=(WIDTH * 10, HEIGHT * 10), interpolation=cv2.INTER_NEAREST_EXACT)

    # 최종 결과를 표현할 배열을 알고리즘 별로 생성
    final_A, final_B, final_C = [], [], []
    for i in range(3):
        tmp_A, tmp_B, tmp_C = [], [], []
        for c in SECTION[i]:
            y, x = c
            if res_A[y][x] == 2:
                tmp_A.append(c)
            if res_B[y][x] == 2:
                tmp_B.append(c)
            if res_C[y][x] == 2:
                tmp_C.append(c)
        if len(tmp_A) > 15:
            tmp_A = random.sample(tmp_A, 15)
        if len(tmp_B) > 15:
            tmp_B = random.sample(tmp_B, 15)
        if len(tmp_C) > 15:
            tmp_C = random.sample(tmp_C, 15)
        final_A.append(tmp_A)
        final_B.append(tmp_B)
        final_C.append(tmp_C)

    ALGOR_DICT = {
        'A': final_A,
        'B': final_B,
        'C': final_C
    }
    lenA, lenB, lenC = 0, 0, 0
    for i in range(len(final_A)):
        arr = final_A[i]
        for j in range(len(arr)):
            lenA += len(arr[j])
    for i in range(len(final_B)):
        arr = final_B[i]
        for j in range(len(arr)):
            lenB += len(arr[j])
    for i in range(len(final_C)):
        arr = final_C[i]
        for j in range(len(arr)):
            lenC += len(arr[j])

    print(f'Writing {model_key}_?.jpg files...')
    cv2.imwrite(f'{model_key}_A.jpg', img_A)
    cv2.imwrite(f'{model_key}_B.jpg', img_B)
    cv2.imwrite(f'{model_key}_C.jpg', img_C)
    """
    res = cv2.vconcat([img_A, img_B, img_C])
    view(res, 1, 'ABC')
    """
    return ALGOR_DICT[algorithm]

"""
def extract_points(algorithm, num, token):
    print(f'{token}...!')
    예시) extract_points('C', 5) 호출 시 구역별 경유지 반환
         : [ [[a, b ], [c, d], ... ],
             [[e, f], [g, h], ... ],
             [[i, j], [k, l], ... ]]
    fin = ALGOR_DICT[algorithm]
    points = [[], [], []]
    tmp = []

    for i in range(3):
        tmp = np.random.choice(np.arange(0, len(fin[i])), num, replace=False)
        for j in tmp:
            points[i].append([fin[i][j][0], fin[i][j][1]])
        print(f'SECTION{i} extracted!: {points[i]}')

    return points
"""

if __name__ == "__main__":
    # Season 0 : SPRING, 1 : SUMMER, 2 : FALL, 3 : WINTER
    for s in range(0, 4):
        # Time 0 : MORNING, 1 : AFTERNOON, 2: EVENING, 3 : MIDNIGHT
        for t in range(0, 4):
            # Weather 0 : SUNNY, 1 : CLOUDY, 3 : RAINY
            for w in range(0, 3):
                extract_points(f'{s}{t}{w}', 'A')
                extract_points(f'{s}{t}{w}', 'B')
                extract_points(f'{s}{t}{w}', 'C')
    view(res, 1, 'ABC')