import json
import random

from individual import Individual


class Population:
    def __init__(self, size, max_weight):
        self.individuals = []
        self.max_weight = max_weight
        self.size = size
        self.adaptation_sum = 0
        self.parents = []
        self.children = []

        # Read data from the JSON file
        with open('data.json', 'r') as file:
            self.backpack = json.load(file)
            self.backpack_size = len(self.backpack["items"])

    def calculate_adaptation(self):
        self.adaptation_sum = 0
        for individual in self.individuals:
            self.adaptation_sum += individual.calculate_adaptation()

    def set_probability_in_population(self):
        for individual in self.individuals:
            individual.set_probability(self.adaptation_sum)

    def get_best_individual(self):
        return max(self.individuals, key=lambda individual: individual.get_cost())

    def remove_individual(self, individual):
        self.individuals.remove(individual)

    def generate_individuals(self):
        for _ in range(self.size):
            self.individuals.append(Individual(self.backpack_size, self.max_weight, self.backpack))

    def single_point_crossing(self, parent_a, parent_b):
        children_a = Individual(self.backpack_size, self.max_weight, self.backpack)
        children_b = Individual(self.backpack_size, self.max_weight, self.backpack)
        crossing_point = random.randint(1, self.backpack_size - 1)

        for index in range(0, crossing_point):
            children_a.set_bit(index, parent_a.get_bits()[index])
            children_b.set_bit(index, parent_b.get_bits()[index])

        for index in range(crossing_point, self.backpack_size):
            children_a.set_bit(index, parent_b.get_bits()[index])
            children_b.set_bit(index, parent_a.get_bits()[index])
        return children_a, children_b

    def two_point_crossing(self, parent_a, parent_b):

        children_a = Individual(self.backpack_size, self.max_weight, self.backpack)
        children_b = Individual(self.backpack_size, self.max_weight, self.backpack)
        while True:
            first_crossing_point = random.randint(1, self.backpack_size - 1)
            second_crossing_point = random.randint(1, self.backpack_size - 1)
            if first_crossing_point != second_crossing_point and abs(first_crossing_point - second_crossing_point) >= 1:
                break

        for index in range(0, min(first_crossing_point, second_crossing_point)):
            children_a.set_bit(index, parent_a.get_bits()[index])
            children_b.set_bit(index, parent_b.get_bits()[index])

        for index in range(min(first_crossing_point, second_crossing_point),
                           max(first_crossing_point, second_crossing_point)):
            children_a.set_bit(index, parent_b.get_bits()[index])
            children_b.set_bit(index, parent_a.get_bits()[index])

        for index in range(max(first_crossing_point, second_crossing_point), self.backpack_size):
            children_a.set_bit(index, parent_a.get_bits()[index])
            children_b.set_bit(index, parent_b.get_bits()[index])
        return children_a, children_b

    def mutation(self, mutation_probability):
        for individual in self.children:
            if random.random() < mutation_probability:
                individual.mutation()

    def roulette_selection(self):
        sections = []
        summ = 0

        # We create sections for each individual in the population
        for index, individual in enumerate(self.individuals):
            sections.append([individual, summ, summ + individual.get_probability()])
            summ += individual.get_probability()

        for _ in range(int(self.size * 0.45)):  # we choose 90% parents by roulette selection
            random_numer = random.uniform(0, 1)
            for section in sections:
                if section[1] < random_numer <= section[2]:
                    self.parents.append(section[0])
                    self.remove_individual(section[0])
                    sections.remove(section)
                    break

    def elite_selection(self):
        self.parents = []
        for _ in range(int(self.size * 0.05)):  # we choose 10% parents by elite_selection
            best_individual = self.get_best_individual()
            self.parents.append(best_individual)
            self.remove_individual(best_individual)

    def choose_parents(self):
        self.parents = []
        self.elite_selection()
        self.roulette_selection()
        self.individuals = self.parents  # new population is made of selected parents and their children

    def generate_children(self, crossover_probability, mutation_probability):
        self.children = []

        for _ in range(len(self.parents) // 2):
            # Use random.sample to pick two distinct parents
            parent_indices = random.sample(range(len(self.parents)), 2)

            parent_a = self.parents[parent_indices[0]]
            parent_b = self.parents[parent_indices[1]]

            if random.random() < crossover_probability:
                if random.random() < 0.70:  # setting single point crossing ratio to two point crossing
                    children_a, children_b = self.single_point_crossing(parent_a, parent_b)
                else:
                    children_a, children_b = self.two_point_crossing(parent_a, parent_b)
            else:
                children_a, children_b = parent_a, parent_b

            self.children.append(children_a)
            self.children.append(children_b)

        self.mutation(mutation_probability)
        for children in self.children:
            self.individuals.append(children)
