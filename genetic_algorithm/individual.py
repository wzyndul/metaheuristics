import random


class Individual:
    def __init__(self, size, max_weight, backpack):
        self.__size = size
        self.__bits = [random.choice([0, 1]) for _ in range(self.__size)]
        self.__probability = 0  # probability of choosing this particular individual
        self.__weight = 0
        self.__max_weight = max_weight
        self.__cost = 0
        self.backpack = backpack
        self.calculate_weight()
        while self.__weight > self.__max_weight: # generate new values if backpack is too heavy
            self.__bits = [random.choice([0, 1]) for _ in range(self.__size)]
            self.calculate_weight()

    def get_bits(self):
        return self.__bits

    def get_probability(self):
        return self.__probability

    def get_weight(self):
        return self.__weight

    def get_cost(self):
        return self.__cost

    def set_bit(self, index, value):
        self.__bits[index] = value

    def calculate_adaptation(self):
        self.__weight = 0
        self.__cost = 0
        for index, bit in enumerate(self.__bits):
            self.__weight += self.backpack["items"][index]["weight"] * bit
            self.__cost += self.backpack["items"][index]["value"] * bit
        if self.__weight > self.__max_weight:
            self.__cost = 0  # set adaptation value (cost) to zero if backpack to heavy
        return self.__cost

    def set_probability(self, adaptation_sum):
        self.__probability = self.__cost / adaptation_sum

    def mutation(self):
        random_bit = random.randint(0, self.__size - 1)
        self.__bits[random_bit] = 1 if self.__bits[random_bit] == 0 else 0

    def calculate_weight(self):
        self.__weight = 0
        for index, bit in enumerate(self.__bits):
            self.__weight += self.backpack["items"][index]["weight"] * bit


