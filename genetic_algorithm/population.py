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
        return max(self.__individuals, key=lambda individual: individual.get_weight())

    def remove_individual(self, individual):
        self.__individuals.remove(individual)

    def generate_individuals(self):
        for _ in range(self.__size):
            self.__individuals.append(Individual(self.__backpack_size, self.__max_weight))

    def single_point_crossing(self, parent_a, parent_b, crossover_probability):
        if random.random() < crossover_probability:
            children_a = Individual(self.__backpack_size, self.__max_weight)
            children_b = Individual(self.__backpack_size, self.__max_weight)
            crossing_point = random.randint(1,
                                            self.__backpack_size - 2)  # wykluczamy wybranie wszystkich genów z 1 rodzica
            for index in range(0, crossing_point):
                children_a.set_bit(index, parent_a.get_bits()[index])
                children_b.set_bit(index, parent_b.get_bits()[index])

            for index in range(crossing_point, self.__backpack_size):
                children_a.set_bit(index, parent_b.get_bits()[index])
                children_b.set_bit(index, parent_a.get_bits()[index])
            return children_a, children_b
        else:
            return parent_a, parent_b

    def two_point_crossing(self, parent_a, parent_b, crossover_probability):
        if random.random() < crossover_probability:
            children_a = Individual(self.__backpack_size, self.__max_weight)
            children_b = Individual(self.__backpack_size, self.__max_weight)
            while True:
                number1 = random.randint(1, self.__backpack_size - 2)
                number2 = random.randint(1, self.__backpack_size - 2)
                if number1 != number2 and abs(number1 - number2) > 2:
                    break
            for index in range(0, min(number1, number2)):
                children_a.set_bit(index, parent_a.get_bits()[index])
                children_b.set_bit(index, parent_b.get_bits()[index])

            for index in range(min(number1, number2), max(number1, number2)):
                children_a.set_bit(index, parent_b.get_bits()[index])
                children_b.set_bit(index, parent_a.get_bits()[index])

            for index in range(max(number1, number2), self.__backpack_size):
                children_a.set_bit(index, parent_a.get_bits()[index])
                children_b.set_bit(index, parent_b.get_bits()[index])
            return children_a, children_b
        else:
            return parent_a, parent_b

    def mutation(self, mutation_probability):
        for individual in self.__children:
            if random.random() < mutation_probability:
                individual.mutation()

    def roulette_selection(self):
        self.__parents = []
        sections = []
        summ = 0

        # We create sections for each individual in the population
        for index, individual in enumerate(self.__individuals):
            sections.append([individual, summ, summ + individual.get_probability()])
            summ += individual.get_probability()

        for _ in range(self.__size / 2):  # we choose half of the population to be the parents
            random_numer = random.uniform(0, 1)
            for section in sections:
                if section[1] < random_numer <= section[2]:
                    self.__parents.append(section[0])
                    self.remove_individual(section[0])
                    break

    def generate_children(self, crossover_probability, mutation_probability):
        self.__children = []

        for _ in range(int(self.__size / 2)): # NA SZYBKO BYLO ROBIONE, nie jest uzyta zadna selekcja
            # Use random.sample to pick two distinct parents
            parent_indices = random.sample(range(self.__size), 2)

            parent_a = self.__individuals[parent_indices[0]]
            parent_b = self.__individuals[parent_indices[1]]

            children_a, children_b = self.single_point_crossing(parent_a, parent_b, crossover_probability)
            self.__children.append(children_a)
            self.__children.append(children_b)

        self.mutation(mutation_probability)
        for children in self.__children:
            self.__individuals.append(children)

