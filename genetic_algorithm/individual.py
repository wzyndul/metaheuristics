import random


class Individual:
    def __init__(self, size, max_weight, backpack):
        self.size = size
        self.bits = [random.choice([0, 1]) for _ in range(self.size)]
        self.probability = 0  # probability of choosing this particular individual
        self.weight = 0
        self.max_weight = max_weight
        self.cost = 0
        self.backpack = backpack
        self.calculate_weight()
        while self.weight > self.max_weight: # generate new values if backpack is too heavy
            self.bits = [random.choice([0, 1]) for _ in range(self.size)]
            self.calculate_weight()


    def calculate_adaptation(self):
        self.weight = 0
        self.cost = 0
        for index, bit in enumerate(self.bits):
            self.weight += self.backpack["items"][index]["weight"] * bit
            self.cost += self.backpack["items"][index]["value"] * bit
        if self.weight > self.max_weight:
            self.cost = 0  # set adaptation value (cost) to zero if backpack to heavy
        return self.cost

    def set_probability(self, adaptation_sum):
        self.probability = self.cost / adaptation_sum

    def mutation(self):
        random_bit = random.randint(0, self.size - 1)
        self.bits[random_bit] = 1 if self.bits[random_bit] == 0 else 0

    def calculate_weight(self):
        self.weight = 0
        for index, bit in enumerate(self.bits):
            self.weight += self.backpack["items"][index]["weight"] * bit


