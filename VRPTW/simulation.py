import copy

from matplotlib import pyplot as plt

from colony import Colony
import pandas as pd
import numpy as np
from node import Node

# vehicle capacity:
# R1, C1, RC1: 200
# R2, RC2: 1000
# C2: 700

NR_ANTS = 30
ALPHA = 0.5
BETA = 3
NR_ITERATIONS = 100
VAPORIZATION_RATE = 0.1
FILE_PATH = "data/R1/R101.csv"
CAPACITY = 200


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


def plot_routes(routes):
    for i, route in enumerate(routes):
        x = [node.x for node in route]
        y = [node.y for node in route]

        plt.plot(x[1:], y[1:], marker='o', label=f'Route {i + 1}')

    plt.plot(x[0], y[0], marker='s', markersize=8, color='black', label='Depot')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Vehicle Routes')
    plt.legend()

    plt.show()


best_solutions = []
for x in range(5):
    best_in_iteration = None
    nodes = load_points_from_file(FILE_PATH)
    for i in range(NR_ITERATIONS):
        ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, copy.deepcopy(nodes), CAPACITY)
        ant_colony.move_ants()
        ant_colony.update_pheromones()

        colony_best_solution = ant_colony.get_best_solution()

        if best_in_iteration is None or colony_best_solution.distance < best_in_iteration.distance:
            best_in_iteration = colony_best_solution
    best_solutions.append(best_in_iteration)

best_all_time = min(best_solutions, key=lambda x: x.distance)
routes = best_all_time.get_routes()
print("Best solution: " + str(best_all_time.distance))
print("Average solution: " + str(np.mean([x.distance for x in best_solutions])))
print(f"Vehicle number in best solution: {best_all_time.vehicles}")

# plot routes for best solution
plot_routes(routes)
