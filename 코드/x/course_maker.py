import cv2
import numpy as np
from collections import defaultdict
from heapq import *
from point_maker import extract_points

WIDTH = 59
HEIGHT = 32

O_LATITUDE = 37.57244364
O_LONGTITUDE = 126.96095890
LAT_GAP = 0.000896694
LONG_GAP = 0.001138112


def shortest_path(start_node, edges, grids):
    mst = []  # 빈 list 선언
    adjacent_edges = defaultdict(list)  # default값이 list인 딕셔너리 (키: 리스트)

    # 키: 각 vertex, 리스트: 키 vertex기준 연결되어있는 vertex들
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set()  # 빈 집합 선언
    connected_nodes.add(start_node)
    candidate_edge_list = adjacent_edges[start_node]  # 시작노드로 후보 엣지 리스트 구성
    heapify(candidate_edge_list)  # 우선순위 큐 구성

    for x in grids:
        while candidate_edge_list:
            weight, n1, n2 = heappop(candidate_edge_list)  # 가장 거리가 짧은 노드 pop
            if n2 not in connected_nodes:  # 연결된 노드에 없다면
                connected_nodes.add(n2)  # connected node에 추가
                mst.append((weight, n1, n2))  # mst에 추가
                break

        candidate_edge_list = adjacent_edges[n2]  # 후보 엣지 리스트 구성
        heapify(candidate_edge_list)  # 우선순위 큐 구성

    return mst


selected_grids = extract_points(algorithm='A', num=6)
idx_result = []
coor_result = []

for grids in selected_grids:
    edges = []

    # (거리, vertex1, vertex2) 형태의 리스트 구현
    for i in range(len(grids)):
        for j in range(i + 1, len(grids)):
            y1, x1 = grids[i]
            y2, x2 = grids[j]
            distance = round((((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1 / 2), 2)
            edges.append((distance, grids[i], grids[j]))

    # print(edges)
    result = shortest_path(grids[0], edges, grids)

    idx_mid_result = []
    coor_mid_result = []
    for distance, idx, x in result:
        y, x = idx
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        string = str(gy) + "," + str(gx)
        idx_mid_result.append(idx)
        coor_mid_result.append(string)

    idx_result.append(idx_mid_result)
    coor_result.append(coor_mid_result)
    # print(idx_mid_result) # 그리드 번호 중간 결과 출력
    # print(coor_mid_result)  # 위도 경도 중간 결과 출력

print(idx_result) # 그리드 번호 결과 출력
print(coor_result) # 위도 경도 결과 출력


ROUTE = idx_result

# 빨 주 노 초 하늘 파 보 갈 회 검
RAINBOW_DICT = {0: [255, 0, 0], 1: [255, 100, 0], 2: [255, 255, 0],
                3: [0, 255, 0], 4: [0, 100, 255], 5: [0, 0, 255],
                6: [100, 0, 255], 7: [139, 69, 19], 8: [105, 105, 105], 9: [0, 0, 0]}

img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)

for section in range(3):
    key = 0
    for num in ROUTE[section]:
        y, x = num
        if section == 0:
            result[y][x][0] = RAINBOW_DICT[key][2]
            result[y][x][1] = RAINBOW_DICT[key][1]
            result[y][x][2] = RAINBOW_DICT[key][0]
        elif section == 1:
            result[y][x][0] = RAINBOW_DICT[key][2]
            result[y][x][1] = RAINBOW_DICT[key][1]
            result[y][x][2] = RAINBOW_DICT[key][0]
        else:
            result[y][x][0] = RAINBOW_DICT[key][2]
            result[y][x][1] = RAINBOW_DICT[key][1]
            result[y][x][2] = RAINBOW_DICT[key][0]
        key += 1

res = cv2.resize(result, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', res)
cv2.waitKey()