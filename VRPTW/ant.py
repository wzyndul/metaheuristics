import math
import random


class Ant:
    def __init__(self, nodes, max_capacity):
        self.distance = 0
        self.nodes = nodes
        self.visited = [nodes[0]]
        self.nodes[0].visited = True
        self.capacity = 0
        self.max_capacity = max_capacity
        self.time = 0
        self.unvisited = None
        self.next_node = None
        self.vehicles = 0

    def calculate_total_distance(self):
        total_distance = 0
        for i in range(len(self.visited) - 1):
            total_distance += math.sqrt(
                (self.visited[i].x - self.visited[i + 1].x) ** 2 +
                (self.visited[i].y - self.visited[i + 1].y) ** 2)
        self.distance = total_distance

    def distance_heuristic(self, node):
        current_node = self.visited[-1]
        return math.sqrt((node.x - current_node.x) ** 2 +
                         (node.y - current_node.y) ** 2)

    def waiting_time_heuristic(self, node):
        arrival_time = self.time + self.distance_heuristic(node)
        waiting_time = max(0, node.ready_time - arrival_time)
        return waiting_time

    def possible_to_visit(self):
        self.unvisited = [node for node in self.nodes if
                          node.visited != True and self.capacity
                          + node.demand <= self.max_capacity and
                          self.time + self.distance_heuristic(node)
                          <= node.due_date and self.time + self.distance_heuristic(node) * 2 + node.service_time <=
                          self.nodes[0].due_date]

    def calculate_probabilities(self, pheromones, alpha, beta):
        sum_denominator = 0
        current_node = self.visited[-1]

        for node in self.unvisited:
            sum_denominator += pheromones[current_node.id - 1][node.id - 1] ** alpha * \
                               (1 / (self.distance_heuristic(node) + self.waiting_time_heuristic(node))) ** beta

        for node in self.unvisited:
            node.probability = (pheromones[current_node.id - 1][node.id - 1] ** alpha * \
                                (1 / (self.distance_heuristic(node) + self.waiting_time_heuristic(
                                    node))) ** beta) / sum_denominator

    def visit(self, pheromones, alpha, beta):
        while len([node for node in self.nodes if node.visited != True]) > 0:
            self.possible_to_visit()
            if len(self.unvisited) == 0:
                self.next_node = self.nodes[0]
                self.time = 0
                self.capacity = 0
            else:
                if random.random() < 0.05:
                    self.next_node = random.choice(self.unvisited)
                else:
                    self.calculate_probabilities(pheromones, alpha, beta)
                    random_number = random.random()
                    sum_probability = 0
                    for node in self.unvisited:
                        sum_probability += node.probability
                        if sum_probability >= random_number:
                            self.next_node = node
                            break
            self.time += self.distance_heuristic(self.next_node)
            self.visited.append(self.next_node)
            self.next_node.visited = True
            self.capacity += self.next_node.demand

            if self.next_node.ready_time > self.time:
                self.time = self.next_node.ready_time
            self.time += self.next_node.service_time
            if self.next_node == self.nodes[0]:
                self.vehicles += 1

    def get_routes(self):
        routes = []
        base = 0
        for i in range(1, len(self.visited)):
            if self.visited[i].id == 1:
                route = (self.visited[base:i + 1])
                table = []
                for node in route:
                    table.append(node)
                routes.append(table)
                base = i

        return routes
