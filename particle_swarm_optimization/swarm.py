from particle import Particle


class Swarm:
    def __init__(self, inertia_rate, cognitive_constant, social_constant,
                 num_particles, function):
        self.best_particle = None
        self.particles = [
            Particle(inertia_rate, cognitive_constant, social_constant,
                     function)
            for _ in range(num_particles)]

    def get_best_particle(self):
        self.best_particle = min(self.particles, key=lambda
            particle: particle.best_adaptation)

    def calculate_adaptation(self):
        for particle in self.particles:
            particle.calculate_adaptation()

    def update_particles(self):
        for particle in self.particles:
            particle.update_velocity(self.best_particle.best_x,
                                     self.best_particle.best_y)
