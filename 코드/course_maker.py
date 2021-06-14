# ================================================
# course_maker.py
# - TSP (또는 Greedy) 알고리즘으로 점의 순서를 합리적으로 지정.
# ================================================

import cv2
import numpy as np

# google OR-Tools(최적화 오픈소스 라이브러리)에서 import
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

from point_maker import extract_points
from const_data import *


''' ↓ 알고리즘, 포인트 개수 입력'''
ALGORITHM = 'C'
POINTS = 9

WIDTH = 59
HEIGHT = 32
O_LATITUDE = 37.57244364
O_LONGTITUDE = 126.96095890
LAT_GAP = 0.000896694
LONG_GAP = 0.001138112

idx_result = []
coor_result = []


# distance matrix 생성하는 함수
def make_distance_matrix(grids):
    distance_matrix = []
    # (거리, vertex1, vertex2) 형태의 리스트 구현
    for i in grids:
        temp = []
        for j in grids:
            y1, x1 = i
            y2, x2 = j
            distance = round((((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1 / 2), 2)
            temp.append(distance)
        distance_matrix.append(temp)
    return distance_matrix


# idx result를 corr(위도, 경도) result로 변경
def idx2coor(idx_result):
    temp = []
    for idx in idx_result:
        x, y = idx
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        string = str(gy) + "," + str(gx)
        temp.append(string)

    return temp


""" Travelling Salesman / Greedy 주석 풀어 바로 사용 """
# <editor-fold desc="Simple travelling salesman problem between cities">
def create_data_model(distance_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def get_routes(solution, routing, manager):
    """Get vehicle routes from a solution and store them in an array."""
    # Get vehicle routes and store them in a two dimensional array whose
    # i,j entry is the jth location visited by vehicle i along its route.
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))
        routes.append(route)
    return routes


def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

def algorithm_by_section(selected_grids):
    idx_result = []
    coor_result = []

    # 구역별로 TSP 알고리즘 실행
    for index in range(len(selected_grids)):
        if len(selected_grids[index]) == 0:
            coor_result.append([])
        else:
            # distance matrix 생성
            distance_matrix = make_distance_matrix(selected_grids[index])

            data = create_data_model(distance_matrix)

            # Create the routing index manager.
            # RoutingIndexManager input
            # distance matrix 행 개수
            # vehicle 개수 (TSP의 경우 차량은 1대)
            # depot인 노드
            manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                                   data['num_vehicles'], data['depot'])

            # Create Routing Model.
            routing = pywrapcp.RoutingModel(manager)

            transit_callback_index = routing.RegisterTransitCallback(distance_callback)

            # Define cost of each arc.
            routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

            # Setting first solution heuristic.
            search_parameters = pywrapcp.DefaultRoutingSearchParameters()
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

            # Solve the problem.
            solution = routing.SolveWithParameters(search_parameters)

            routes = get_routes(solution, routing, manager)
            # Display the routes.
            # for i, route in enumerate(routes):
            #    print('Route', i, route)

            idx_temp = []
            coor_temp = []

            # index result
            for j in range(len(routes[0]) - 1):
                idx_temp.append(selected_grids[index][routes[0][j]])
            idx_result.append(idx_temp)

            # coordinate result
            coor_temp = idx2coor(idx_temp)
            coor_result.append(coor_temp)

    return coor_result

def main():
    """Entry point of the program."""

    ### make text file
    waypoints_f = open("waypoints.txt", 'w')
    startpoints_f = open("startpoints.txt", 'w')

    waypoints_f.write("$waypoints = array(\n")
    startpoints_f.write("$start = array(\n")

    # Instantiate the data
    # season
    for s in range(0, 4):
        waypoints_f.write("\tarray(\n")
        startpoints_f.write("\tarray(\n")
        # time
        for t in range(0, 4):
            waypoints_f.write("\t\tarray(\n")
            startpoints_f.write("\t\tarray(\n")
            # weather
            for w in range(0, 3):
                waypoints_f.write("\t\t\tarray(\n")
                startpoints_f.write("\t\t\tarray(\n")
                model = str(s) + str(t) + str(w)
                PREDICT = MODEL_DICT[model]

                A_coor_result = []
                B_coor_result = []
                C_coor_result = []

                # A B C 알고리즘 수행
                for alg in ['A', 'B', 'C']:
                    ALGORITHM = alg
                    print(alg)

                    # 히트맵에서 thresholding 한 결과
                    print(model)
                    selected_grids = extract_points(PREDICT, ALGORITHM)

                    coor_result = []
                    coor_result = algorithm_by_section(selected_grids)

                    #print(idx_result)
                    #print(coor_result)
                    if alg == 'A':
                        A_coor_result = coor_result
                    if alg == 'B':
                        B_coor_result = coor_result
                    if alg == 'C':
                        C_coor_result = coor_result

                print('A ' + str(A_coor_result))
                print('B ' + str(B_coor_result))
                print('C ' + str(C_coor_result))

                # print course to a course.txt file
                for i in range(0, 3):
                    # section
                    waypoints_f.write("\t\t\t\tarray(\n")

                    # A algorithm
                    waypoints_f.write("\t\t\t\t\tarray(")
                    startpoints_f.write("\t\t\t\tarray(")
                    startpoints_f.write('\'' + str(A_coor_result[i][0]) + '\',')

                    for j in range(1, len(A_coor_result[i])):
                        if j == len(A_coor_result[i]) - 1:
                            waypoints_f.write('\'' + str(A_coor_result[i][j]) + '\'')
                        else:
                            waypoints_f.write('\'' + str(A_coor_result[i][j]) + '\', ')
                    waypoints_f.write('),\n')

                    # B algorithm
                    # B 알고리즘 결과가 빈 배열([])이면 A 루트 가져옴.
                    if len(B_coor_result[i]) == 0:
                        B_coor_result[i] = A_coor_result[i]

                    waypoints_f.write("\t\t\t\t\tarray(")
                    startpoints_f.write('\'' + str(B_coor_result[i][0]) + '\',')

                    for j in range(1, len(B_coor_result[i])):
                        if j == len(B_coor_result[i]) - 1:
                            waypoints_f.write('\'' + str(B_coor_result[i][j]) + '\'')
                        else:
                            waypoints_f.write('\'' + str(B_coor_result[i][j]) + '\', ')
                    waypoints_f.write('),\n')

                    # C algorithm
                    # C 알고리즘 결과가 빈 배열([])이면 A 루트 가져옴.
                    if len(C_coor_result[i]) == 0:
                        C_coor_result[i] = A_coor_result[i]

                    waypoints_f.write("\t\t\t\t\tarray(")
                    startpoints_f.write('\'' + str(C_coor_result[i][0]) + '\'')

                    for j in range(len(C_coor_result[i])):
                        if j == len(C_coor_result[i]) - 1:
                            waypoints_f.write('\'' + str(C_coor_result[i][j]) + '\'')
                        else:
                            waypoints_f.write('\'' + str(C_coor_result[i][j]) + '\', ')
                    waypoints_f.write(')\n')
                    #startpoints_f.write(')\n')

                    if i == 2:
                        waypoints_f.write('\t\t\t\t)\n')
                        startpoints_f.write(')\n')
                    else:
                        waypoints_f.write('\t\t\t\t),\n')
                        startpoints_f.write('),\n')

                if w == 2:
                    waypoints_f.write('\t\t\t)\n')
                    startpoints_f.write('\t\t\t)\n')
                else:
                    waypoints_f.write('\t\t\t),\n')
                    startpoints_f.write('\t\t\t),\n')

            if t == 3:
                waypoints_f.write('\t\t)\n')
                startpoints_f.write('\t\t)\n')
            else:
                waypoints_f.write('\t\t),\n')
                startpoints_f.write('\t\t),\n')

        if s == 3:
            waypoints_f.write('\t)\n')
            startpoints_f.write('\t)\n')
        else:
            waypoints_f.write('\t),\n')
            startpoints_f.write('\t),\n')

    waypoints_f.write(');\n')
    startpoints_f.write(');\n')

    waypoints_f.close()
    startpoints_f.close()

# </editor-fold>
# <editor-fold desc="Greedy Algorithm">
'''
from collections import defaultdict
from heapq import *

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
'''
# </editor-fold>


if __name__ == '__main__':
    main()

# 빨 → 주 → 노 → 초 → 파 → 보 → 연회 → 회 → 진회 → 검정
RAINBOW_DICT = {0: [255, 0, 0], 1: [255, 100, 0], 2: [255, 255, 0],
                3: [0, 255, 0], 4: [0, 0, 255], 5: [100, 0, 255],
                6: [204, 204, 204], 7: [153, 153, 153], 8: [102, 102, 102], 9: [0, 0, 0]}

ROUTE = idx_result
img = cv2.imread("img/grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)

for section in range(3):
    key = 0
    for num in ROUTE[section]:
        y, x = num
        img[y][x][0] = RAINBOW_DICT[key][2]
        img[y][x][1] = RAINBOW_DICT[key][1]
        img[y][x][2] = RAINBOW_DICT[key][0]
        key += 1
        if key > 9:
            break

res = cv2.resize(img, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', res)
cv2.waitKey()

