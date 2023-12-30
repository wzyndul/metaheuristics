import random


class Particle:
    def __init__(self, inertia_rate, cognitive_constant, social_constant,
                 function):
        self.x = random.uniform(-10, 10)
        self.y = random.uniform(-10, 10)
        self.velocity = [0, 0]
        self.inertia_rate = inertia_rate
        self.cognitive_constant = cognitive_constant
        self.social_constant = social_constant
        self.best_x = self.x
        self.best_y = self.y
        self.best_adaptation = float("inf")
        self.function = function
        self.adaptation = float("inf")

    def calculate_adaptation(self):
        self.adaptation = self.function(self.x, self.y)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_x = self.x
            self.best_y = self.y

    def update_velocity(self, global_best_x, global_best_y):
        r1 = random.random()
        r2 = random.random()
        self.velocity[0] = self.inertia_rate * self.velocity[
            0] + self.cognitive_constant * r1 * (
                                   self.best_x - self.x) + self.social_constant * r2 * (
                                   global_best_x - self.x)
        self.velocity[1] = self.inertia_rate * self.velocity[
            1] + self.cognitive_constant * r1 * (
                                   self.best_y - self.y) + self.social_constant * r2 * (
                                   global_best_y - self.y)

        self.x += self.velocity[0]
        self.y += self.velocity[1]
