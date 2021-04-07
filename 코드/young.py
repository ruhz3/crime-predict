import numpy as np
import cv2
import openpyxl
import random


WIDTH = 59
HEIGHT = 32

DONG_DICT = {
    0: '중림동', 1: '소공동', 2: '회현동', 3: '명동',  4: '필동', 5: '을지로동',
    6: '장충동', 7: '광희동', 8: '다산동', 9: '약수동', 10: '신당동', 11: '청구동',
    12: '동화동', 13: '신당5동', 14: '황학동'
}

COLOR_DICT = {
    0: [54, 182, 229], 1: [176, 228, 239], 2: [21, 0, 136], 3: [127, 127, 127], 4: [14, 201, 255], 5: [29, 230, 181],
    6: [164, 73, 163], 7: [87, 122, 185], 8: [232, 162, 0], 9: [201, 174, 255], 10: [76, 177, 34], 11: [0, 242, 255],
    12: [39, 127, 255], 13: [204, 72, 63], 14: [36, 28, 237]
}

FLOAT_ARR = [
    [12170,   32230,   41700,   19220],
    [32870,   87020,   112600,   51900],
    [18260,   48340,   62550,   28830],
    [24350,   64450,   83410,   38450],
    [29220,   77350,   100090,   46140],
    [30440,   80570,   104260,   48060],
    [10350,   27390,   35450,   16340],
    [48700,   128920,   166820,   76900],
    [91320,   241720,   312790,   144190],
    [111400, 294900, 381610, 175910],
    [90710,   240110,   310710,   143220],
    [59050,   156310,   202270,   93240],
    [68790,   182100,   235640,   108620],
    [73660,   194990,   252320,   116310],
    [51740,   136970,   177250,   81700]
]

# 그리드 이미지를 배열로 변환
img = cv2.imread("222.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)

# 그리드를 동별로 분리
grids_dong = []
for i in range(15):
    new = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if img[y][x][0] == COLOR_DICT[i][0] and img[y][x][1] == COLOR_DICT[i][1] and img[y][x][2] == COLOR_DICT[i][2]:
                new.append([x, y])
    grids_dong.append(new)

# 엑셀 파일 생성(연도별 시트 생성)
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = "Grid"
sheet['B1'] = "Time"
sheet['C1'] = "Float"

# 시간대별로 그리드 생성
grid_morning = np.zeros(shape=(WIDTH, HEIGHT), dtype=int)
grid_afternoon = np.zeros(shape=(WIDTH, HEIGHT), dtype=int)
grid_evening = np.zeros(shape=(WIDTH, HEIGHT), dtype=int)
grid_midnight = np.zeros(shape=(WIDTH, HEIGHT), dtype=int)

def make_data(grid, time):
    # i 동, time 시간에서
    for i in range(15):
        case_num = FLOAT_ARR[i][time]
        l = len(grids_dong[i])
        for j in range(case_num/10):
            n = random.randrange(1, l+1)
            x, y = grids_dong[i][n]
            grid[y][x] += 10
    
grid_morning = make_data(grid_morning, 0)
print(grid_morning)

num = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        if grid_morning[y][x] == 0:
            continue
