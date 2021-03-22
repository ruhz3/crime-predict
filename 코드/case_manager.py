import cv2
import random
import openpyxl


''' ↓ 저장할 엑셀 파일 이름, 원점 그리드의 GPS 좌표입력'''
FILE_NAME = "crime_data_x"
O_LATITUDE = 37.5727023
O_LONGTITUDE = 126.961014

LONG_GAP = 0.0011314
LAT_GAP = 0.0008914
WIDTH = 59
HEIGHT = 32



# 그리드 이미지를 배열로 변환
img = cv2.imread("grid.png", 0)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)


# 배경이 아닌 그리드의 좌표만 배열에 따로 저장 [위도, 경도]
grids = []
for i in range(WIDTH):
    for j in range(HEIGHT):
        if img[j][i] == 255 :
            img[j][i] = 0
        else :
            img[j][i] = 255
            grids.append([j, i])


# 엑셀 파일 생성
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = "Type"
sheet['B1'] = "Date-Time"
sheet['C1'] = "Latitude"
sheet['D1'] = "Longitude"


# 2행 부터 2202행 까지,
for i in range(2, 2202):
    # 범죄유형
    sheet.cell(row=i, column=1).value = "절도"

    # 범죄시간
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    sheet.cell(row=i, column=2).value = date + " " + time

    # 범죄지점 : 그리드 좌표 중 랜덤한 구역을 정하고, 그 구역 안에서 랜덤생성
    idx = int(random.uniform(0, len(grids)))
    x, y = grids[idx]
    gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
    sheet.cell(row=i, column=3).value = random.uniform(gx - LAT_GAP, gx)
    sheet.cell(row=i, column=4).value = random.uniform(gy, gy + LONG_GAP)


# 파일 저장
wb.save(FILE_NAME + '.xlsx')


# 배열이 이미지와 같게 구성되었는지 확인
result = cv2.resize(dsize=(WIDTH*10, HEIGHT*10), src=img)
cv2.imshow("res", result)
cv2.waitKey()


