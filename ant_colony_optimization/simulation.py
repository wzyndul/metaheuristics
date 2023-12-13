import sys

from attraction import Attraction
from colony import Colony
from matplotlib.lines import Line2D
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
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='skyblue', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[ant.visited[0].id], node_color='green', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[ant.visited[-1].id], node_color='red', node_size=700)
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax, font_weight='bold', font_color='black')

    limits = plt.axis('on')
    ax.axis('off')

    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Początek', markerfacecolor='green', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='Koniec', markerfacecolor='red', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='Węzły odwiedzone po drodze', markerfacecolor='skyblue', markersize=10)]
    ax.legend(handles=legend_elements, loc='best')

    plt.show()


attractions = load_points_from_file(FILE_PATH)
best_out_of_five = []
total_distance = 0
for round_number in range(5):
    best_ant = None
    for i in range(NR_ITERATIONS):
        ant_colony = Colony(NR_ANTS, ALPHA, BETA, VAPORIZATION_RATE, attractions)
        ant_colony.move_ants()
        ant_colony.update_pheromones()
        if best_ant is None or ant_colony.find_best_ant().distance < best_ant.distance:
            best_ant = ant_colony.find_best_ant()
            print(f"Próba {round_number + 1}, Iteracja {i + 1}: Najkrótsza długość trasy: {best_ant.distance}")
    print(f"Koniec próby {round_number + 1}")
    best_out_of_five.append(best_ant)
    total_distance += best_ant.distance

average_distance = total_distance / 5
print(f"Średna długość tras mrówek po 5 próbach: {average_distance}")

overall_best_ant = min(best_out_of_five, key=lambda ant: ant.distance)
create_movement_graph(overall_best_ant)
print(f"Najkrótsza długość trasy najlepszej mrówki z 5 prób: {overall_best_ant.distance}")
