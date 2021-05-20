# ================================================
# testcase.py
# - 테스트 케이스 생성
# ================================================

import numpy as np
import random
from section_maker import SECTION
from module import num2coord
from const_data import *


TESTCASE = 450
GRID_NUM = 1107
RANDOM = [3731, 3454, 3084, 2684, 2530, 2827]
ARTIFICIAL = [3000, 3000, 3000, 3000, 3000, 3000]

# 어떤 모델을 불러올지 결정
'''
time = input()
'''
time = 2

# 테스트케이스 수에 맞춰 랜덤, 인공 데이터 개수 결정
r = int(np.average(np.array(RANDOM)))
a = 3000
random_case = round(TESTCASE * r / (r+a))
artificial_case = round(TESTCASE * a / (r+a))

# 인공 데이터를 넣을 그리드를 구역별로 분류
print("dividing in section...")

# danger_grids_and = [[구역0 예상 위험지역], [구역1 예상 위험지역], [구역2 예상 위험지역]]
danger_grids_and = [[], [], []]
for i in DANGER_GRID_AND[time]:
    b, a = num2coord[i]
    if [b, a] in SECTION[0]:
        danger_grids_and[0].append(i)
    elif [b, a] in SECTION[1]:
        danger_grids_and[1].append(i)
    elif [b, a] in SECTION[2]:
        danger_grids_and[2].append(i)

# danger_grids_or = [[구역0 예상 위험지역], [구역1 예상 위험지역], [구역2 예상 위험지역]]
danger_grids_or = [[], [], []]
for i in DANGER_GRID_OR[time]:
    b, a = num2coord[i]
    if [b, a] in SECTION[0]:
        danger_grids_or[0].append(i)
    elif [b, a] in SECTION[1]:
        danger_grids_or[1].append(i)
    elif [b, a] in SECTION[2]:
        danger_grids_or[2].append(i)

# 결정한 개수대로 그리드 안에서 생성하자
test_cases = []
grd_switch = False
for i in range(3):
    tmp = []
    for j in range(random_case):
        idx = int(random.uniform(0, len(SECTION[i])))
        x, y = SECTION[i][idx]
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        point = f'{random.uniform(gy, gy + LONG_GAP)}, {random.uniform(gx - LAT_GAP, gx)}'
        tmp.append(point)
    for j in range(artificial_case):
        # AND와 OR을 번갈아가면서 넣을 것
        if grd_switch:
            gg = danger_grids_and[i]
        else:
            gg = danger_grids_or[i]

        # 하지만 만약 배열이 비어있다면 그냥 랜덤 생성
        if len(gg) != 0:
            grd_switch = (grd_switch == False)
            ii = int(random.uniform(0, len(gg)))
            idx = gg[ii]
            x, y = num2coord[idx]
        else:
            idx = int(random.uniform(0, len(SECTION[i])))
            x, y = SECTION[i][idx]

        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        point = f'{random.uniform(gy, gy + LONG_GAP)}, {random.uniform(gx - LAT_GAP, gx)}'
        tmp.append(point)
    test_cases.append(tmp)

# 결과 출력
for i in range(3):
    print(f'SECTION{i}({len(test_cases[i])}개) : {test_cases[i]}')