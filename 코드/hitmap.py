# ================================================
# hitmap.py
# - 예측한 결과를 지도 위에 히트맵으로 시각화
# ================================================

import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from const_data import *
from module import *
from section_maker import SECTION

WIDTH = 59
HEIGHT = 32
GRID_NUM = 1107

# 그리드 이미지를 배열로 변환
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)


def hitmap_image(arr=None, map=None, section=False):
    """
    히트맵 이미지를 반환합니다.
    :param arr: 범죄 예측 배열
    :param map: 범죄 예측 지도
    :param section: 구역별 색상차이 옵션
    :return: 이미지 배열
    """
    # map 형태로 들어왔다면, 배열로 바꿔주자!
    if map is not None:
        tmp = []
        for i in range(GRID_NUM):
            y, x = num2coord[i]
            tmp.append(int(map[y][x]))
        CRIME_PREDICT = tmp
    else:
        CRIME_PREDICT = arr

    result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)
    if section:
        # 색상 딕셔너리 생성
        new_0, new_1, new_2 = {}, {}, {}
        for i in range(256):
            new_0[i] = [255, 128 - int(i/2), 128 - int(i/2)]
            new_1[i] = [128 - int(i/2), 255, 128 - int(i/2)]
            new_2[i] = [128 - int(i/2), 128 - int(i/2), 255]

        # 구역별로 색상 값을 매핑
        grid_color = np.empty(shape=(1107, 3), dtype=np.uint8)
        for i in range(3):
            histogram = np.zeros(256, np.float_)
            for j in SECTION[i]:
                y, x = j
                n = coord2num[y][x]
                histogram[CRIME_PREDICT[n]] += 1  # Make Histogram!
            for j in range(256):
                histogram[j] /= len(SECTION[i])  # Normalize it!
            for j in range(1, 256):
                histogram[j] += histogram[j - 1]  # Accumulate it!
            for j in range(1, 256):
                histogram[j] = round(histogram[j] * 255)  # Convert to int(round)!
            for j in SECTION[i]:
                y, x = j
                n = coord2num[y][x]
                key = int(histogram[CRIME_PREDICT[n]])  # 0 to 255
                if i == 0:
                    grid_color[n] = new_0[key]
                elif i == 1:
                    grid_color[n] = new_1[key]
                elif i == 2:
                    grid_color[n] = new_2[key]
                '''
                if key <= 255 and key >= 235:  # 235 is Threshold!
                    grid_color[j] = new_d[key]
                else:
                    grid_color[j] = new_d[0]
                '''

    else:
        # 색상 딕셔너리 생성
        color_dict = {}
        for i in range(256):
            color_dict[i] = [255, 128 - int(i / 2), 128 - int(i / 2)]

        # 히스토그램 생성
        grid_color = []
        histogram = np.zeros(256, np.float_)
        for i in range(GRID_NUM):
            histogram[CRIME_PREDICT[i]] += 1  # Make histogram!
        for i in range(256):
            histogram[i] /= GRID_NUM  # Normalize it!
        for i in range(1, 256):
            histogram[i] += histogram[i - 1]  # Accumulate it!
        for i in range(1, 256):
            histogram[i] = round(histogram[i] * 255)  # Convert to int(round)!
        for i in CRIME_PREDICT:
            key = int(histogram[i])
            grid_color.append(color_dict[key])

    # 결정된 색상을 result[]에 입혀줌
    for i in range(GRID_NUM):
        y, x = num2coord[i]
        result[y][x][0] = grid_color[i][2]
        result[y][x][1] = grid_color[i][1]
        result[y][x][2] = grid_color[i][0]

    return result


def point_image(arr):
    """
    지정한 점을 그리드 위에 그립니다.
    :param arr: [[2, 3], [14, 0], ...]
    :return:  이미지 배열
    """
    result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            result[y][x] = img[y][x]
    for p in arr:
        y, x = p
        result[y][x] = [0, 0, 255]
    return result


def view(image, times, winname):
    H, W, n = image.shape
    image = cv2.resize(image, dsize=(W * times, H * times), interpolation=cv2.INTER_NEAREST_EXACT)
    cv2.imshow(winname, image)
    cv2.waitKey()


def bar_graph(arr, name):
    x = np.arange(0, 256)
    y = arr
    sns.barplot(x=x, y=y)
    plt.title(name, fontsize='20')
    plt.show()

'''
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
'''



