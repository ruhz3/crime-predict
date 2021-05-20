import cv2
import numpy as np

WIDTH = 59
HEIGHT = 32
ROUTE = [[11, 12, 247, 77, 78, 26, 146, 91, 386, 381, 40, 42, 221, 340, 343, 227, 228, 56],
         [483, 484, 651, 852, 853, 681, 741, 802, 576, 577],
         [779, 959, 1024, 975, 1047, 1050, 873, 938, 888]]
section_dict = {
    0: [200, 100, 100],
    1: [100, 200, 100],
    2: [100, 100, 200]
}

# 구역별로 색상을 다르게 매핑하기 위한 딕셔너리 생성
color_dict_0 = {}
color_dict_1 = {}
color_dict_2 = {}
for i in range(25):
    color_dict_0[i] = [255, 255 - i * 8, 255 - i * 8]
    color_dict_1[i] = [255 - i * 8, 255, 255 - i * 8]
    color_dict_2[i] = [255 - i * 8, 255 - i * 8, 255]

# 그리드 배열 불러오기
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)

# 그리드 번호를 좌표로 매핑할 배열
# : num2coord['그리드 번호'] = 좌표의 y, x값 반환
num2coord = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            num2coord.append([y, x])

# 좌표 번호를 그리드 좌표로 반환
# : coord2num['y 좌표']['x 좌표'] = 그리드 번호 반환
# : 해당 좌표가 배경이라면 -1 반환
coord2num = np.full((HEIGHT, WIDTH), -1)
idx = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            coord2num[y][x] = idx
            idx += 1

# 경유지의 좌표를 색상 순서대로 매핑
for section in range(3):
    key = 0
    for num in ROUTE[section]:
        y, x = num2coord[num]
        if section == 0:
            img[y][x][0] = color_dict_0[key][2]
            img[y][x][1] = color_dict_0[key][1]
            img[y][x][2] = color_dict_0[key][0]
        elif section == 1:
            img[y][x][0] = color_dict_1[key][2]
            img[y][x][1] = color_dict_1[key][1]
            img[y][x][2] = color_dict_1[key][0]
        else:
            img[y][x][0] = color_dict_2[key][2]
            img[y][x][1] = color_dict_2[key][1]
            img[y][x][2] = color_dict_2[key][0]
        key += 1

# 시각화
res = cv2.resize(img, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', res)
cv2.waitKey()