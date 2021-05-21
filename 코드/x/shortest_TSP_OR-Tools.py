import cv2
import numpy as np
from point_maker import extract_points

WIDTH = 59
HEIGHT = 32

O_LATITUDE = 37.57244364
O_LONGTITUDE = 126.96095890
LAT_GAP = 0.000896694
LONG_GAP = 0.001138112

idx_result = []
coor_result = []

num2coord = []
img = cv2.imread("grid.png", 0)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x] != 255:
            num2coord.append([y, x])

# distance matrix 생성하는 함수
def make_distance_matrix(grids):
    distance_matrix = []

    # (거리, vertex1, vertex2) 형태의 리스트 구현
    for i in range(len(grids)):
        temp = []
        for j in range(len(grids)):
            y1, x1 = num2coord[grids[i]]
            y2, x2 = num2coord[grids[j]]
            distance = round((((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1 / 2), 2)
            temp.append(distance)

        distance_matrix.append(temp)

    return distance_matrix

# idx result를 corr(위도, 경도) result로 변경
def idx2coor(idx_result):
    temp = []
    for idx in idx_result:
        y, x = num2coord[idx]
        gx, gy = O_LATITUDE - x * LAT_GAP, O_LONGTITUDE + y * LONG_GAP
        string = str(gy) + "," + str(gx)
        temp.append(string)

    return temp

"""Simple travelling salesman problem between cities."""

# google OR-Tools(최적화 오픈소스 라이브러리)에서 import
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model(distance_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix
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
    selected_grids = extract_points('C', 9)

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
        #if solution:
        #    print_solution(manager, routing, solution)

        routes = get_routes(solution, routing, manager)
        # Display the routes.
        #for i, route in enumerate(routes):
        #    print('Route', i, route)

        idx_temp = []
        for j in range(len(routes[0]) - 1):
            idx_temp.append(selected_grids[index][routes[0][j]])
        idx_result.append(idx_temp)
        coor_temp = idx2coor(idx_temp)
        print(coor_temp)
        coor_result.append(coor_temp)

    print(idx_result)
    print(coor_result)


if __name__ == '__main__':
    main()

ROUTE = idx_result

section_dict = {
    0: [200, 100, 100],
    1: [100, 200, 100],
    2: [100, 100, 200]
}
color_dict_0 = {}
for i in range(25):
    color_dict_0[i] = [255, 255 - i * 8, 255 - i * 8]
color_dict_1 = {}
for i in range(25):
    color_dict_1[i] = [255 - i * 8, 255, 255 - i * 8]
color_dict_2 = {}
for i in range(25):
    color_dict_2[i] = [255 - i * 8, 255 - i * 8, 255]

# 빨 주 노 초 파 보 연회색 회색 진회색 검은색
rainbow_color_dict = {0: [255, 0, 0], 1: [255, 100, 0], 2: [255, 255, 0],
                      3: [0, 255, 0], 4: [0, 0, 255], 5: [100, 0, 255],
                      6: [204, 204, 204], 7: [153, 153, 153], 8: [102, 102, 102], 9: [0, 0, 0]}

img = cv2.imread("grid.png", 1)
img = cv2.resize(dsize=(WIDTH, HEIGHT), src=img)
result = np.full((HEIGHT, WIDTH, 3), 255, np.uint8)


num2grid = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        if img[y][x][0] != 255 or img[y][x][1] != 255 or img[y][x][2] != 255:
            num2grid.append([y, x])

for section in range(3):
    key = 0
    for num in ROUTE[section]:
        y, x = num2grid[num]
        if section == 0:
            img[y][x][0] = rainbow_color_dict[key][2]
            img[y][x][1] = rainbow_color_dict[key][1]
            img[y][x][2] = rainbow_color_dict[key][0]
        elif section == 1:
            img[y][x][0] = rainbow_color_dict[key][2]
            img[y][x][1] = rainbow_color_dict[key][1]
            img[y][x][2] = rainbow_color_dict[key][0]
        else:
            img[y][x][0] = rainbow_color_dict[key][2]
            img[y][x][1] = rainbow_color_dict[key][1]
            img[y][x][2] = rainbow_color_dict[key][0]
        key += 1

res = cv2.resize(img, dsize=(WIDTH*20, HEIGHT*20), interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imshow('res', res)
cv2.waitKey()

