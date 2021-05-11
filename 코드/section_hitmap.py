from dong_clsfy import *
import matplotlib.pyplot as plt


def conv(image, kernel, padding=1, strides=1):
    xImgShape, yImgShape = image.shape
    xKernShape, yKernShape = kernel.shape

    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
    else:
        imagePadded = image

    for y in range(yImgShape):
        if y > yImgShape - yKernShape:
            break
        if y % strides == 0:
            for x in range(xImgShape):
                if x > xImgShape - xKernShape:
                    break
                try:
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break
    return output


# 모델이 생성한 결과 * 10
FIRST_PREDICT = [2, 3, 2, 2, 2, 2, 2, 0, 0, 3, 2, 3, 2, 1, 2, 2, 2, 0, 0, 1, 3, 2, 2, 2, 3, 2, 3, 1, 1, 1, 2, 2, 1, 3, 1, 3, 0,
                 1, 2, 3, 1, 2, 2, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 3, 2, 2, 3, 1, 0, 1, 1, 2, 2, 1, 2, 0, 2, 0, 0, 2, 2, 0, 0, 1,
                 2, 1, 2, 2, 2, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 2, 1, 2, 2, 1, 2, 1, 1,
                 0, 0, 3, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 0, 0, 0, 1, 2, 2, 0, 0, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2,
                 0, 1, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 2, 0, 2, 0, 2, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0,
                 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 3, 2, 0, 3, 0, 3, 2, 1, 1, 1, 0, 2, 1, 0, 2, 0, 1, 3,
                 0, 0, 0, 0, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 1, 1, 0, 2, 0, 2, 3, 1, 1, 3, 2, 3, 3, 0, 1, 0, 0, 2, 2, 1, 1, 0, 2,
                 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 2, 2, 2, 2, 1, 0, 3, 2, 0, 0, 0, 3,
                 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 0, 2, 2, 0, 2, 0, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 0, 0, 0, 0, 0, 2,
                 0, 0, 1, 0, 0, 2, 2, 3, 2, 2, 2, 2, 0, 0, 0, 0, 3, 2, 2, 0, 0, 0, 2, 2, 2, 2, 3, 3, 2, 3, 0, 1, 0, 1, 2, 1, 0,
                 1, 2, 1, 2, 3, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 3, 1, 1, 2, 2, 1, 0, 2, 3, 1, 2, 1, 1, 2, 2, 1, 1, 0, 1, 1, 0,
                 0, 1, 1, 0, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1, 1, 0, 2, 0, 0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0,
                 1, 0, 0, 1, 0, 0, 0, 1, 0, 2, 3, 1, 2, 2, 3, 2, 2, 2, 3, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 3, 0, 2, 2, 1, 1, 2, 3,
                 2, 2, 3, 4, 2, 1, 1, 1, 0, 1, 1, 1, 1, 0, 2, 3, 1, 2, 3, 2, 3, 2, 2, 2, 3, 2, 1, 1, 1, 2, 1, 0, 1, 1, 1, 0, 0,
                 1, 1, 2, 0, 0, 1, 1, 0, 3, 0, 3, 3, 2, 1, 1, 1, 2, 1, 1, 0, 1, 0, 1, 2, 1, 1, 0, 0, 0, 2, 1, 2, 0, 2, 2, 2, 2,
                 2, 1, 2, 4, 2, 1, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1, 2, 0, 2, 3, 2, 3, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0,
                 0, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 1, 1, 2, 1, 2, 1, 1, 1,
                 4, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 0, 2, 1, 4, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 0, 2, 0, 0,
                 0, 0, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 0, 2,
                 2, 2, 1, 2, 1, 1, 2, 2, 0, 0, 0, 1, 4, 2, 0, 2, 2, 0, 2, 6, 3, 5, 1, 1, 0, 1, 1, 0, 2, 1, 0, 1, 0, 0, 2, 2, 0,
                 2, 4, 1, 4, 2, 5, 2, 5, 3, 5, 5, 5, 4, 4, 2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 0, 2, 2, 0, 2, 0, 4, 3, 2, 2, 0, 1,
                 6, 4, 5, 2, 7, 5, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 4, 1, 2, 2, 2, 0, 1, 5, 3, 5, 1, 2, 5, 3, 5, 5, 5, 2, 2,
                 3, 0, 3, 0, 0, 1, 4, 1, 1, 1, 7, 2, 4, 6, 1, 1, 5, 3, 3, 4, 2, 3, 6, 3, 6, 4, 0, 2, 2, 0, 0, 2, 1, 4, 1, 4, 4,
                 4, 6, 4, 1, 1, 0, 1, 1, 2, 2, 1, 4, 5, 5, 1, 3, 5, 3, 1, 2, 3, 2, 5, 1, 1, 1, 2, 5, 2, 1, 1, 2, 2, 1, 0, 1, 0,
                 5, 5, 2, 0, 5, 2, 3, 2, 2, 2, 2, 5, 1, 7, 0, 1, 3, 1, 7, 3, 1, 2, 1, 1, 5, 2, 7, 4, 2, 2, 3, 1, 0, 1, 3, 1, 0,
                 3, 4, 3, 2, 3, 3, 0, 2, 0, 2, 3, 5, 5, 1, 4, 1, 3, 2, 3, 2, 5, 2, 2, 5, 1, 2, 5, 2, 2, 3, 2, 1, 2, 5, 4, 4, 1,
                 3, 1, 3, 1, 1, 2, 2, 1, 5, 1, 3, 2, 3, 5, 6, 5, 7, 4, 3, 1, 3, 2, 2, 1, 1, 2, 3, 6, 5, 3, 3, 3, 3, 7, 4, 6, 1,
                 3, 2, 1, 1, 1, 2, 2, 5, 2, 2, 2, 5, 1, 3, 7, 3, 2, 2, 1, 2, 1, 3, 1, 2, 0, 2, 3, 0, 1, 4, 5, 6, 3, 3, 4, 2, 2,
                 1, 2, 2, 0, 5, 6, 2, 2, 5, 5, 5, 6, 2, 3, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 5, 5, 5, 5, 5, 2, 3, 1, 4, 1, 2, 1, 2,
                 5, 5, 2, 2, 6, 5, 5, 5, 6, 3, 2, 3, 0, 2, 3, 2, 3, 1, 3, 2, 2, 4, 4, 5, 5, 4, 5, 4, 6, 5, 3, 5, 6, 5]
for i in range(1107):
    FIRST_PREDICT[i] = FIRST_PREDICT[i]*10

# 구역별로 그리드 번호를 분할
DONG = get_dong_array()
SECTION = []
tmp = []
for i in range(0, 15):
    for j in DONG[i]:
        tmp.append(j)
    if i == 3 or i == 8 or i == 14:
        tmp.sort()
        SECTION.append(tmp)
        tmp = []
'''
<막대 그래프로 표현>
for s in range(3):
    x = np.arange(len(SECTION[s]))
    y = []
    for i in SECTION[s]:
        y.append(CRIME_PREDICT[i])
    plt.bar(x, y)
    plt.show()
'''
WIDTH = 59
HEIGHT = 32
GRID_NUM = 1107
'''
<5x5 Kernel>
LPF = [[1/36, 1/36, 1/36, 1/36, 1/36],
       [1/36, 2/36, 2/36, 2/36, 1/36],
       [1/36, 2/36, 4/36, 2/36, 1/36],
       [1/36, 2/36, 2/36, 2/36, 1/36],
       [1/36, 1/36, 1/36, 1/36, 1/36]]
'''
LPF = [[1/10, 1/10, 1/10],
       [1/10, 2/10, 1/10],
       [1/10, 1/10, 1/10]]

SECTION_DICT = {
    2: [255, 100, 50],
    1: [50, 255, 100],
    0: [100, 50, 255]
}

# 색상 딕셔너리 생성(총 256단계)
new_0 = {}
new_1 = {}
new_2 = {}
for i in range(256):
    new_0[i] = [255, 255 - i, 255 - i]
for i in range(256):
    new_1[i] = [255 - i, 255, 255 - i]
for i in range(256):
    new_2[i] = [255 - i, 255 - i, 255]

# 그리드 이미지를 배열로 변환
grid = []
img = cv2.imread("grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            grid.append([y, x])

# 모델이 생성한 결과를 그리드 배열판에 올림
map = np.zeros(shape=(HEIGHT, WIDTH))
idx = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            map[y][x] = FIRST_PREDICT[idx]
            idx += 1

# 배열판에 올린 숫자들을 LPF로 뭉개줌
CRIME_PREDICT = []
map = conv(map, np.array(LPF), padding=1)

for i in range(1107):
    y, x = grid[i]
    CRIME_PREDICT.append(int(map[y][x]))

# 그리드 별로 색상을 결정
grid_color = np.empty(shape=(1107, 3), dtype=np.uint8)
for i in range(3):
    histogram = np.zeros(256, np.float_)
    for j in SECTION[i]:
        histogram[CRIME_PREDICT[j]] += 1    # Make Histogram!
    for j in range(256):
        histogram[j] /= len(SECTION[i])  # Normalize it!
    for j in range(1, 256):
        histogram[j] += histogram[j - 1]  # Accumulate it!
    for j in range(1, 256):
        histogram[j] = round(histogram[j] * 255)  # Convert to int(round)!
    for j in SECTION[i]:
        key = int(histogram[CRIME_PREDICT[j]])  # 0 to 255
        if i == 0:
            grid_color[j] = new_0[key]
        elif i == 1:
            grid_color[j] = new_1[key]
        elif i == 2:
            grid_color[j] = new_2[key]
        '''
        if key <= 255 and key >= 235:  # 235 is Threshold!
            grid_color[j] = new_d[key]
        else:
            grid_color[j] = new_d[0]
        '''
        crime_img = np.full((HEIGHT, WIDTH), -1, np.uint8)

# 결정된 색상을 result[]에 입혀줌
for i in range(GRID_NUM):
    y, x = grid[i]
    result[y][x][0] = grid_color[i][2]
    result[y][x][1] = grid_color[i][1]
    result[y][x][2] = grid_color[i][0]

'''
<구역별 색상표시>
for i in range(3):
    for j in SECTION[i]:
        color = SECTION_DICT[i]
        y, x = grid[j]
        result[y][x][0] = color[2]
        result[y][x][1] = color[1]
        result[y][x][2] = color[0]
'''

A_KERNEL = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
for x in range(WIDTH):
    for y in range(HEIGHT):

# 결과 맵을 확대해서 출력
result = cv2.resize(result, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', result)
cv2.waitKey()
