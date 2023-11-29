import json
import random

from individual import Individual


class Population:
    def __init__(self, size, max_weight):
        self.__individuals = []
        self.__max_weight = max_weight
        self.__size = size
        self.__adaptation_sum = 0
        self.__parents = []
        self.__children = []

        # Read data from the JSON file
        with open('data.json', 'r') as file:
            self.backpack = json.load(file)
            self.__backpack_size = len(self.backpack["items"])

    def calculate_adaptation(self, backpack):
        self.__adaptation_sum = 0
        for individual in self.__individuals:
            self.__adaptation_sum += individual.calculate_adaptation(backpack)


    def set_probability_in_population(self):
        for individual in self.__individuals:
            individual.set_probability(self.__adaptation_sum)

    def get_best_individual(self):
        return max(self.__individuals, key=lambda individual: individual.get_cost())

    def remove_individual(self, individual):
        self.__individuals.remove(individual)

    def generate_individuals(self):
        for _ in range(self.__size):
            self.__individuals.append(Individual(self.__backpack_size, self.__max_weight))

    def single_point_crossing(self, parent_a, parent_b):
            children_a = Individual(self.__backpack_size, self.__max_weight)
            children_b = Individual(self.__backpack_size, self.__max_weight)
            crossing_point = random.randint(1,
                                            self.__backpack_size - 2)  # wykluczamy wybranie wszystkich genów z 1 rodzica
            # print("Crossing point: ", crossing_point)
            for index in range(0, crossing_point):
                children_a.set_bit(index, parent_a.get_bits()[index])
                children_b.set_bit(index, parent_b.get_bits()[index])

            for index in range(crossing_point, self.__backpack_size):
                children_a.set_bit(index, parent_b.get_bits()[index])
                children_b.set_bit(index, parent_a.get_bits()[index])
            return children_a, children_b


    def two_point_crossing(self, parent_a, parent_b):

        children_a = Individual(self.__backpack_size, self.__max_weight)
        children_b = Individual(self.__backpack_size, self.__max_weight)
        while True:
            first_crossing_point = random.randint(1, self.__backpack_size - 2)
            second_crossing_point = random.randint(1, self.__backpack_size - 2)
            if first_crossing_point != second_crossing_point and abs(first_crossing_point - second_crossing_point) > 2:
                break
        # print("First crossing point: ", first_crossing_point)
        # print("Second crossing point: ", second_crossing_point)
        for index in range(0, min(first_crossing_point, second_crossing_point)):
            children_a.set_bit(index, parent_a.get_bits()[index])
            children_b.set_bit(index, parent_b.get_bits()[index])

        for index in range(min(first_crossing_point, second_crossing_point), max(first_crossing_point, second_crossing_point)):
            children_a.set_bit(index, parent_b.get_bits()[index])
            children_b.set_bit(index, parent_a.get_bits()[index])

        for index in range(max(first_crossing_point, second_crossing_point), self.__backpack_size):
            children_a.set_bit(index, parent_a.get_bits()[index])
            children_b.set_bit(index, parent_b.get_bits()[index])
        return children_a, children_b


    def mutation(self, mutation_probability):
        for individual in self.__children:
            if random.random() < mutation_probability:
                individual.mutation()

    def roulette_selection(self):
        sections = []
        summ = 0

        # We create sections for each individual in the population
        for index, individual in enumerate(self.__individuals):
            sections.append([individual, summ, summ + individual.get_probability()])
            summ += individual.get_probability()

        for _ in range(int(self.__size * 0.4)):  # we choose half of the population to be the parents
            random_numer = random.uniform(0, 1)
            for section in sections:
                if section[1] < random_numer <= section[2]:
                    self.__parents.append(section[0])
                    self.remove_individual(section[0])
                    sections.remove(section)
                    break

    def elite_selection(self):
        self.__parents = []
        for _ in range(int(self.__size * 0.1)):
            best_individual = self.get_best_individual()
            self.__parents.append(best_individual)
            self.remove_individual(best_individual)

    def choose_parents(self):
        self.__parents = []
        self.elite_selection()
        self.roulette_selection()
        self.__individuals = self.__parents


    def generate_children(self, crossover_probability, mutation_probability):
        self.__children = []

        for _ in range(len(self.__parents) // 2):
            # Use random.sample to pick two distinct parents
            parent_indices = random.sample(range(len(self.__parents)), 2)

            parent_a = self.__parents[parent_indices[0]]
            parent_b = self.__parents[parent_indices[1]]

            if random.random() < crossover_probability:
                if random.random() < 0.7:  # USTAWIAM PROPORCJE KRZYZOWANIA
                    children_a, children_b = self.single_point_crossing(parent_a, parent_b)
                else:
                    children_a, children_b = self.two_point_crossing(parent_a, parent_b)
            else:
                children_a, children_b = parent_a, parent_b

            self.__children.append(children_a)
            self.__children.append(children_b)

        self.mutation(mutation_probability)
        for children in self.__children:
            self.__individuals.append(children)
