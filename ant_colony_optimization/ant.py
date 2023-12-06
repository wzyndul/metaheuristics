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

        # Add the distance from the last attraction back to the starting attraction
        first_attraction = self.visited[0]
        last_attraction = self.visited[-1]
        total_distance += math.sqrt((last_attraction.x - first_attraction.x) ** 2 +
                                    (last_attraction.y - first_attraction.y) ** 2)

        self.distance = total_distance

    def distance_to_attraction(self, attraction):
        current_attraction = self.visited[-1]
        return math.sqrt((attraction.x - current_attraction.x) ** 2 +
                         (attraction.y - current_attraction.y) ** 2)

    def visit_with_probability(self, pheromones, alpha, beta):
        pass

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
        current_attraction = self.visited[-1]
        unvisited_attractions = [attraction for attraction in self.attractions if attraction not in self.visited]
        probabilities = []
        sum_denominator = 0
        numerator = 1

