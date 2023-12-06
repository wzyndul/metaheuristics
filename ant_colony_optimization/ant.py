import math
import random


class Ant:
    def __init__(self, attractions):
        self.distance = 0
        self.attractions = attractions
        self.visited = [random.choice(attractions)]

    def calculate_total_distance(self):
        total_distance = 0
        for i in range(len(self.visited) - 1):
            current_attraction = self.visited[i]
            next_attraction = self.visited[i + 1]
            distance = math.sqrt((next_attraction.x - current_attraction.x) ** 2 +
                                 (next_attraction.y - current_attraction.y) ** 2)
            total_distance += distance

        # z ostatniej atrakcji do 1 nie musimy
        # first_attraction = self.visited[0]
        # last_attraction = self.visited[-1]
        # total_distance += math.sqrt((last_attraction.x - first_attraction.x) ** 2 +
        #                             (last_attraction.y - first_attraction.y) ** 2)

        self.distance = total_distance

    def distance_to_attraction(self, attraction):
        current_attraction = self.visited[-1]
        return math.sqrt((attraction.x - current_attraction.x) ** 2 +
                         (attraction.y - current_attraction.y) ** 2)

    def visit_with_probability(self, pheromones, alpha, beta):
        unvisited_attractions = self.calculate_probabilities(pheromones, alpha, beta)
        random_number = random.random()
        sum_probability = 0
        for attraction in unvisited_attractions:
            sum_probability += attraction.probability
            if sum_probability >= random_number:
                self.visited.append(attraction)
                break

    def visit(self, pheromones, alpha, beta):
        if random.random() < 0.3:  # probability of visiting random attraction
            self.visit_random()
        else:
            self.visit_with_probability(pheromones, alpha, beta)

    def visit_random(self):
        unvisited_attractions = [attraction for attraction in self.attractions if attraction not in self.visited]
        attraction = random.choice(unvisited_attractions)
        self.visited.append(attraction)

    def calculate_probabilities(self, pheromones, alpha, beta):
        unvisited_attractions = [attraction for attraction in self.attractions if attraction not in self.visited]
        sum_denominator = 0
        current_attraction = self.visited[-1]
        for attraction in unvisited_attractions:
            sum_denominator += pheromones[current_attraction.id - 1][attraction.id - 1] ** alpha * \
                               (1 / self.distance_to_attraction(attraction)) ** beta

        for attraction in unvisited_attractions:
            attraction.probability = (pheromones[current_attraction.id - 1][attraction.id - 1] ** alpha * \
                                      (1 / self.distance_to_attraction(attraction)) ** beta) / sum_denominator

        return unvisited_attractions
