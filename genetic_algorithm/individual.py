import random


class Individual:
    def __init__(self, size, max_weight):
        self.__size = size
        self.__bits = [random.choice([0, 1]) for _ in range(self.__size)]
        self.__probability = 0
        self.__weight = 0
        self.__max_weight = max_weight
        self.__cost = 0
    def get_size(self):
        return self.__size

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

    def calculate_adaptation(self, backpack):
        self.__weight = 0
        self.__cost = 0
        for index, bit in enumerate(self.__bits):
            self.__weight += backpack["items"][index]["weight"] * bit
            self.__cost += backpack["items"][index]["value"] * bit
        if self.__weight > self.__max_weight:
            self.__weight = 0
        return self.__weight

    def set_probability(self, adaptation_sum):
        self.__probability = self.__weight / adaptation_sum

    def mutation(self):
        random_bit = random.randint(0, self.__size - 1)
        self.__bits[random_bit] = 1 if self.__bits[random_bit] == 0 else 0





