from ant import Ant
import copy


class Colony:
    def __init__(self, nr_ants, alpha, beta, vaporization_rate, nodes, max_capacity):
        self.nr_ants = nr_ants
        self.alpha = alpha
        self.beta = beta
        self.max_capacity = max_capacity
        self.nodes = nodes
        self.nodes[0].visited = True
        self.ants = [Ant(self.nodes, self.max_capacity) for _ in range(self.nr_ants)]
        self.pheromones = [[1 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]
        self.vaporization_rate = vaporization_rate

    def update_pheromones(self):
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones[i])):
                self.pheromones[i][j] = self.pheromones[i][j] * self.vaporization_rate
        for ant in self.ants:
            ant.calculate_total_distance()
            for i in range(len(ant.visited) - 1):
                current_node = ant.visited[i]
                next_node = ant.visited[i + 1]
                self.pheromones[current_node.id - 1][next_node.id - 1] += 1 / ant.distance

    def move_ants(self):
        for ant in self.ants:
            not_visited = [node for node in self.nodes if not node.visited]
            while not ant.visit(self.pheromones, self.alpha, self.beta):
                pass

