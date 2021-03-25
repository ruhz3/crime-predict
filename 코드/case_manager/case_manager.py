import numpy as np
import cv2
import random
import openpyxl


''' ↓ 저장할 엑셀 파일 이름 입력'''
FILE_NAME = "crime_data_x"

O_LATITUDE = 37.5727023
O_LONGTITUDE = 126.961014
LAT_GAP = 0.0008914
LONG_GAP = 0.0011314

WIDTH = 59
HEIGHT = 32

CRIME_KEY = {'절도': 0, '폭행': 1, '살인': 2, '강간': 3, '강도': 4}
YEAR_KEY = {'2014': 0, '2015': 1, '2016': 2, '2017': 3, '2018': 4, '2019': 5,}
CRIME_TOTAL = [5231, 4954, 4584, 4184, 4030, 4327]
CRIME_STATS = [
    [0.4924, 0.9541, 0.9552, 0.9975, 1.0000],
    [0.5143, 0.9633, 0.9639, 0.9982, 1.0000],
    [0.4690, 0.9544, 0.9551, 0.9983, 1.0000],
    [0.4412, 0.9338, 0.9340, 0.9978, 1.0000],
    [0.4602, 0.9454, 0.9459, 0.9973, 1.0000],
    [0.5089, 0.9531, 0.9535, 0.9986, 1.0000]
]


# 그리드 이미지를 배열로 변환
img = cv2.imread("grid.png", 0)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)


# 배경이 아닌 그리드의 좌표만 배열에 따로 저장 [위도, 경도]
grids = []
result = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
for i in range(WIDTH):
    for j in range(HEIGHT):
        if img[j][i] != 255:
            grids.append([j, i])


# 엑셀 파일 생성(연도별 시트 생성)
wb = openpyxl.Workbook()
for y in range(2014, 2019):
    year = f'{y}'
    sheet = wb.create_sheet(year)
    sheet['A1'] = "Type"
    sheet['B1'] = "Date-Time"
    sheet['C1'] = "Latitude"
    sheet['D1'] = "Longitude"
    sheet['E1'] = "Grid"
    case_num = CRIME_TOTAL[YEAR_KEY[year]]

    # 통계자료에 맞춰 범죄사례를 생성
    for i in range(2, case_num + 2):
        # 범죄유형
        n = random.random()
        if n < CRIME_STATS[YEAR_KEY[year]][CRIME_KEY['절도']]:
            type = '절도'
        elif n < CRIME_STATS[YEAR_KEY[year]][CRIME_KEY['폭행']]:
            type = '폭행'
        elif n < CRIME_STATS[YEAR_KEY[year]][CRIME_KEY['살인']]:
            type = '살인'
        elif n < CRIME_STATS[YEAR_KEY[year]][CRIME_KEY['강간']]:
            type = '강간'
        elif n < CRIME_STATS[YEAR_KEY[year]][CRIME_KEY['강도']]:
            type = '강도'
        sheet.cell(row=i, column=1).value = type

        # 범죄시간
        date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
        time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
        sheet.cell(row=i, column=2).value = date + " " + time

        # 범죄지점 : 그리드를 랜덤으로 선택하고, 그리드 내부에서 랜덤생성
        idx = int(random.uniform(0, len(grids)))
        x, y = grids[idx]
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        sheet.cell(row=i, column=3).value = random.uniform(gx - LAT_GAP, gx)
        sheet.cell(row=i, column=4).value = random.uniform(gy, gy + LONG_GAP)
        sheet.cell(row=i, column=5).value = idx


# 파일 저장
wb.remove(wb['Sheet'])
wb.save(FILE_NAME + '.xlsx')
print('Excel file created!')


