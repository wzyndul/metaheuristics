import sys

from attraction import Attraction
from colony import Colony
import networkx as nx
import matplotlib.pyplot as plt

NR_ANTS = int(sys.argv[1])
ALPHA = int(sys.argv[2])
BETA = int(sys.argv[3])
NR_ITERATIONS = int(sys.argv[4])
VAPORIZATION_RATE = float(sys.argv[5])
FILE_PATH = sys.argv[6]


def load_points_from_file(file_path):
    attractions_file = []
    with open("data/" + file_path, 'r') as file:
        for line in file:
            data = line.split()
            identifier = int(data[0])
            x = int(data[1])
            y = int(data[2])
            attractions_file.append(Attraction(identifier, x, y))
    return attractions_file


def create_movement_graph(ant):
    G = nx.Graph()

    for attraction in ant.attractions:
        G.add_node(attraction.id, pos=(attraction.x, attraction.y))

    for i in range(len(ant.visited) - 1):
        current_attraction = ant.visited[i]
        next_attraction = ant.visited[i + 1]
        G.add_edge(current_attraction.id, next_attraction.id)

    pos = nx.get_node_attributes(G, 'pos')
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, pos, ax=ax, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue',
            font_color='black')

    limits = plt.axis('on')
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

    plt.show()


attractions = load_points_from_file(FILE_PATH)
best_out_of_five = []
for round_number in range(5):
    best_ant = None
    for i in range(NR_ITERATIONS):
        ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, attractions)
        ant_colony.move_ants()
        ant_colony.update_pheromones()
        if best_ant is None or ant_colony.find_best_ant().distance < best_ant.distance:
            best_ant = ant_colony.find_best_ant()
            print(f"Round {round_number + 1}, Iteration {i + 1}: Best ant's distance is {best_ant.distance}")
    print(f"After round {round_number + 1}, number of ants: {len(ant_colony.ants)}")
    best_out_of_five.append(best_ant)

overall_best_ant = min(best_out_of_five, key=lambda ant: ant.distance)
create_movement_graph(overall_best_ant)
print(f"The overall best ant has a distance of {overall_best_ant.distance}")
