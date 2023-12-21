from swarm import Swarm


def sphere(x, y):
    return x ** 2 + y ** 2


def booth(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2

swarm = Swarm(0.5, 1.5, 1.5, 10, booth)
for _ in range(100):
    swarm.calculate_adaptation()
    swarm.get_best_particle()
    print(f"best: {swarm.best_particle.best_adaptation}")
    swarm.update_particles()
