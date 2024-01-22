import math
import random


class Ant:
    def __init__(self, nodes, max_capacity):
        self.distance = 0
        self.nodes = nodes
        self.visited = [nodes[0]]
        self.capacity = 0
        self.max_capacity = max_capacity
        self.reached = False
        # print("len nodes", len(self.nodes))
        # print(self.nodes[0].id, self.nodes[0].visited)
        # print(self.nodes[1].id, self.nodes[1].visited)

    def calculate_total_distance(self):
        total_distance = 0
        for i in range(len(self.visited) - 1):
            current_node = self.visited[i]
            next_node = self.visited[i + 1]
            distance = math.sqrt((next_node.x - current_node.x) ** 2 +
                                 (next_node.y - current_node.y) ** 2)
            total_distance += distance

        self.distance = total_distance # I added as last item depot

    def distance_to_node(self, node):
        current_node = self.visited[-1]
        return math.sqrt((node.x - current_node.x) ** 2 +
                         (node.y - current_node.y) ** 2)

    def visit_with_probability(self, pheromones, alpha, beta):
        unvisited_nodes = self.calculate_probabilities(pheromones, alpha, beta)
        if len(unvisited_nodes) == 0:
            self.visited.append(self.nodes[0])
            self.reached = True
        random_number = random.random()
        sum_probability = 0
        for node in unvisited_nodes:
            sum_probability += node.probability
            if sum_probability >= random_number:
                self.visited.append(node)
                self.capacity += node.demand
                self.nodes[node.id - 1].visited = True
                break

    def visit(self, pheromones, alpha, beta):
        if random.random() < 0.3:  # probability of visiting random node
            self.visit_random()
        else:
            self.visit_with_probability(pheromones, alpha, beta)
        return self.reached

    def visit_random(self):
        unvisited_nodes = [node for node in self.nodes if
                           node.visited != True and self.capacity + node.demand <= self.max_capacity]

        if len(unvisited_nodes) == 0:
            self.visited.append(self.nodes[0])
            self.reached = True
            return
        node = random.choice(unvisited_nodes)
        self.visited.append(node)
        self.capacity += node.demand
        self.nodes[node.id - 1].visited = True

    def calculate_probabilities(self, pheromones, alpha, beta):
        unvisited_nodes = [node for node in self.nodes if
                           node.visited != True and self.capacity + node.demand <= self.max_capacity]

        sum_denominator = 0
        current_node = self.visited[-1]

        for node in unvisited_nodes:
            sum_denominator += pheromones[current_node.id - 1][node.id - 1] ** alpha * \
                               (1 / self.distance_to_node(node)) ** beta

        for node in unvisited_nodes:
            node.probability = (pheromones[current_node.id - 1][node.id - 1] ** alpha * \
                                      (1 / self.distance_to_node(node)) ** beta) / sum_denominator
        return unvisited_nodes

