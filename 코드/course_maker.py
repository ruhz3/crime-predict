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


''' ↓ 알고리즘, 포인트 개수 입력'''
ALGORITHM = 'A'
POINTS = 5

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
        y, x = idx
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        string = str(gy) + "," + str(gx)
        temp.append(string)
    coor_result.append(temp)
    return coor_result


""" Travelling Salesman / Greedy 주석 풀어 바로 사용 """
# <editor-fold desc="Simple travelling salesman problem between cities">
def create_data_model(distance_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix
    '''[
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ] ''' # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


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


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    
    # 히트맵에서 thresholding 한 결과
    selected_grids = extract_points(ALGORITHM, POINTS)

    for index in range(len(selected_grids)):
        # distance matrix 생성
        distance_matrix = make_distance_matrix(selected_grids[index])

        data = create_data_model(distance_matrix)

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                               data['num_vehicles'], data['depot'])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)

        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        # if solution:
        #    print_solution(manager, routing, solution)

        routes = get_routes(solution, routing, manager)
        # Display the routes.
        # for i, route in enumerate(routes):
        #    print('Route', i, route)

        idx_temp = []
        for j in range(len(routes[0]) - 1):
            idx_temp.append(selected_grids[index][routes[0][j]])
        idx_result.append(idx_temp)
        coor_temp = idx2coor(idx_temp)
        coor_result.append(coor_temp)

    print(idx_result)
    print(coor_result)
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

res = cv2.resize(img, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', res)
cv2.waitKey()

