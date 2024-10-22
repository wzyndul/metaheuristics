from ant import Ant
import copy


class Colony:
    def __init__(self, nr_ants, alpha, beta, vaporization_rate, nodes, max_capacity):
        self.nr_ants = nr_ants
        self.alpha = alpha
        self.beta = beta
        self.max_capacity = max_capacity
        self.nodes = nodes
        self.ants = [Ant(copy.deepcopy(self.nodes), self.max_capacity) for _ in range(self.nr_ants)]
        self.pheromones = [[0.01 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]
        self.vaporization_rate = vaporization_rate

    def update_pheromones(self):
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones[i])):
                self.pheromones[i][j] *= (1 - self.vaporization_rate)
        for ant in self.ants:
            ant.calculate_total_distance()
            pheromone_deposit = 1 / ant.distance
            for i in range(len(ant.visited) - 1):
                current_node = ant.visited[i]
                next_node = ant.visited[i + 1]
                self.pheromones[current_node.id - 1][next_node.id - 1] += pheromone_deposit

    def move_ants(self):
        for ant in self.ants:
            ant.visit(self.pheromones, self.alpha, self.beta)


    def get_best_solution(self):
        best_ant = self.ants[0]
        for ant in self.ants:
            if ant.distance < best_ant.distance:
                best_ant = ant
        return best_ant