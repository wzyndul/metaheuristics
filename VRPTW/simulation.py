import sys
from colony import Colony
import pandas as pd
import numpy as np

from node import Node

# vehicle capacity:
# R1, C1, RC1: 200
# R2, RC2: 1000
# C2: 700

NR_ANTS = 5
ALPHA = 1
BETA = 1
NR_ITERATIONS = 1000
VAPORIZATION_RATE = 0.5
FILE_PATH = "data/C1/C101.csv"
# FIRST NODE IS DEPOT

def load_points_from_file(file_path):
    names = ['id', 'x', 'y', 'demand', 'ready_time', 'due_time', 'service_time']
    df = pd.read_csv(file_path, delimiter=',', header=0, names=names)
    nodes = []
    for index, row in df.iterrows():
        nodes.append(
            Node(row['id'], row['x'], row['y'], row['demand'], row['ready_time'], row['due_time'], row['service_time']))
    return nodes



nodes = load_points_from_file(FILE_PATH)
import matplotlib.pyplot as plt
x = []
y = []
for node in nodes:
    x.append(node.x)
    y.append(node.y)
plt.scatter(x, y)
plt.show()

# total_distance = 0
# best_ant = None
# for i in range(NR_ITERATIONS):
#     ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, attractions)
#     ant_colony.move_ants()
#     ant_colony.update_pheromones()
#     if best_ant is None or ant_colony.find_best_ant().distance < best_ant.distance:
#         best_ant = ant_colony.find_best_ant()
