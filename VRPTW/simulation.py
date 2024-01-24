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
NR_ITERATIONS = 100
VAPORIZATION_RATE = 0.15
FILE_PATH1 = "data/C1/C101.csv"
FILE_PATH2 = "data/C2/C204.csv"
FILE_PATH3 = "data/R1/R104.csv"
FILE_PATH4 = "data/R2/R210.csv"
FILE_PATH5 = "data/RC1/RC104.csv"
FILE_PATH6 = "data/RC2/RC201.csv"

paths = [FILE_PATH1, FILE_PATH2, FILE_PATH3, FILE_PATH4, FILE_PATH5, FILE_PATH6]


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


for path in paths:
    all_time_best_solution = None
    nodes = load_points_from_file(path)
    for i in range(NR_ITERATIONS):
        ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, copy.deepcopy(nodes), 200)
        ant_colony.move_ants()
        ant_colony.update_pheromones()

        colony_best_solution = ant_colony.get_best_solution()
        routes = colony_best_solution.get_routes()
        if all_time_best_solution is None or colony_best_solution.distance < all_time_best_solution.distance:
            all_time_best_solution = colony_best_solution

    print("Best solution for file " + path + " is: " + str(all_time_best_solution.distance))
