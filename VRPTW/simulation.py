import copy
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

NR_ANTS = 10
ALPHA = 1
BETA = 1
NR_ITERATIONS = 100
VAPORIZATION_RATE = 0.5
FILE_PATH = "data/C1/C101.csv"


# FIRST NODE IS DEPOT

def load_points_from_file(file_path):
    names = ['id', 'x', 'y', 'demand', 'ready_time', 'due_time', 'service_time']
    df = pd.read_csv(file_path, delimiter=',', names=names)
    nodes = []
    for index, row in df.iterrows():
        nodes.append(
            Node(int(row['id']), int(row['x']), int(row['y']), int(row['demand']), int(row['ready_time']), int(row['due_time']), int(row['service_time'])))
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

for i in range(NR_ITERATIONS):
    ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, copy.deepcopy(nodes), 200)
    ant_colony.move_ants()
    ant_colony.update_pheromones()

    # Create a new plot for each iteration
    if i == 1:
        plt.figure()

        for ant_index, ant in enumerate(ant_colony.ants):
            x = []
            y = []
            table = []
            for node in ant.visited:
                table.append(node.id)
                x.append(node.x)
                y.append(node.y)
            print("ant", ant_index + 1)
            print(table)
            print("length", len(table))
            # Plot the path of the current ant with a different color
            plt.scatter(x, y, label=f'Ant {ant_index + 1}', color=COLORS[ant_index])

        plt.legend()
        plt.title(f'Iteration {i + 1}')
        plt.show()
