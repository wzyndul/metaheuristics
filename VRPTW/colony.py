from ant import Ant
import copy

class Colony:
    def __init__(self, nr_ants, alpha, beta, vaporization_rate, attractions):
        self.nr_ants = nr_ants
        self.alpha = alpha
        self.beta = beta
        self.attractions = attractions
        self.ants = [Ant(copy.deepcopy(self.attractions)) for i in range(self.nr_ants)]
        self.pheromones = [[1 for i in range(len(self.attractions))] for j in range(len(self.attractions))]
        self.vaporization_rate = vaporization_rate

    def update_pheromones(self):
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones[i])):
                self.pheromones[i][j] = self.pheromones[i][j] * self.vaporization_rate
        for ant in self.ants:
            ant.calculate_total_distance()
            for i in range(len(ant.visited) - 1):
                current_attraction = ant.visited[i]
                next_attraction = ant.visited[i + 1]
                self.pheromones[current_attraction.id - 1][next_attraction.id - 1] += 1 / ant.distance

    def move_ants(self):
        for x in range(len(self.attractions) - 1):
            for ant in self.ants:
                ant.visit(self.pheromones, self.alpha, self.beta)

    def find_best_ant(self):
        return min(self.ants, key=lambda ant: ant.distance)
