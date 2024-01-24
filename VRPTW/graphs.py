import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from node import Node

FILE_PATH = "data/RC2/RC208.csv"


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

G = nx.Graph()
for node in nodes:
    G.add_node(node.id, pos=(node.x, node.y))

pos = nx.get_node_attributes(G, 'pos')
nx.draw_networkx_nodes(G, pos, node_color='b', node_size=50)
nx.draw_networkx_nodes(G, pos, nodelist=[1], node_color='r', node_size=50)  # depot
plt.show()
