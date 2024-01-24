import copy
import math
import sys
from colony import Colony
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from node import Node

# vehicle capacity:
# R1, C1, RC1: 200
# R2, RC2: 1000
# C2: 700

NR_ANTS = 30
ALPHA = 1
BETA = 2
NR_ITERATIONS = 1000
VAPORIZATION_RATE = 0.25
FILE_PATH = "data/C1/C101.csv"


# FIRST NODE IS DEPOT

def load_points_from_file(file_path):
    names = ['id', 'x', 'y', 'demand', 'ready_time', 'due_time', 'service_time']
    df = pd.read_csv(file_path, delimiter=',', names=names)
    nodes = []
    for index, row in df.iterrows():
        nodes.append(
            Node(int(row['id']), int(row['x']), int(row['y']), int(row['demand']), int(row['ready_time']),
                 int(row['due_time']), int(row['service_time'])))
    return nodes


nodes = load_points_from_file(FILE_PATH)

# x = []
# y = []
# for node in nodes:
#     x.append(node.x)
#     y.append(node.y)
# plt.scatter(x, y)
# plt.show()
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'yellow', 'black', 'brown', 'gray']

all_time_best_solution = None
for i in range(NR_ITERATIONS):
    ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, copy.deepcopy(nodes), 200)
    ant_colony.move_ants()
    ant_colony.update_pheromones()

    colony_best_solution = ant_colony.get_best_solution()
    routes = colony_best_solution.get_routes()
    # print(routes)
    # print(f'Iteration {i + 1}: {colony_best_solution.distance}')
    # print(f'Number of vehicles: {colony_best_solution.vehicles}')
    if all_time_best_solution is None or colony_best_solution.distance < all_time_best_solution.distance:
        all_time_best_solution = colony_best_solution
        print(f"iteration: {i}")
        print(f"New best solution: {all_time_best_solution.distance}")
        print(f'Number of vehicles: {all_time_best_solution.vehicles}')



