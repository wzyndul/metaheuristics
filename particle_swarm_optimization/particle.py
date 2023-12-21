import random


class Particle:
    def __init__(self, inertia_rate, cognitive_constant, social_constant,
                 function):
        self.x = random.uniform(-10, 10)
        self.y = random.uniform(-10, 10)
        self.velocity = 0
        self.inertia_rate = inertia_rate
        self.cognitive_constant = cognitive_constant
        self.social_constant = social_constant
        self.best_x = self.x
        self.best_y = self.y
        self.best_adaptation = float("inf")
        self.function = function

    def calculate_adaptation(self):
        adaptation = self.function(self.x, self.y)
        if adaptation < self.best_adaptation:
            self.best_adaptation = adaptation
            self.best_x = self.x
            self.best_y = self.y

    def euclidean_distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def update_velocity(self, global_best_x, global_best_y):
        r1 = random.random()
        r2 = random.random()

        cognitive_term = self.cognitive_constant * r1 * self.euclidean_distance(
            self.best_x, self.best_y, self.x, self.y)
        social_term = self.social_constant * r2 * self.euclidean_distance(
            global_best_x, global_best_y, self.x, self.y)

        self.velocity = self.inertia_rate * self.velocity + cognitive_term + social_term

        self.x += self.velocity
        self.y += self.velocity
