import sys
import matplotlib.pyplot as plt
from swarm import Swarm

FUNCTION = sys.argv[1]
INERTIA_RATE = float(sys.argv[2])  # 0-1
COGNITIVE_CONSTANT = float(sys.argv[3])  # 0-2
SOCIAL_CONSTANT = float(sys.argv[4])  # 0-2
NUM_PARTICLES = int(sys.argv[5])
NUM_ITERATIONS = int(sys.argv[6])


def sphere(x, y):
    return x ** 2 + y ** 2


def booth(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


best_values_over_iterations = []
best_positions_over_iterations = []

for i in range(5):
    if FUNCTION == "sphere":
        swarm = Swarm(INERTIA_RATE, COGNITIVE_CONSTANT, SOCIAL_CONSTANT,
                      NUM_PARTICLES, sphere)
    else:
        swarm = Swarm(INERTIA_RATE, COGNITIVE_CONSTANT, SOCIAL_CONSTANT,
                      NUM_PARTICLES, booth)

    iteration_values = []
    for _ in range(NUM_ITERATIONS):
        swarm.calculate_adaptation()
        swarm.get_best_particle()
        iteration_values.append(swarm.best_particle.best_adaptation)
        best_positions_over_iterations.append((swarm.best_particle.best_x, swarm.best_particle.best_y))
        swarm.update_particles()
    best_values_over_iterations.append(iteration_values)

plt.figure(figsize=(10, 6))
for i, values in enumerate(best_values_over_iterations, start=1):
    plt.plot(range(1, NUM_ITERATIONS + 1), values, label=f'Eksperyment {i}', linewidth=2)

plt.title('Zmiana najlepszego rozwiazania w czasie')
plt.xlabel('Iteracje')
plt.ylabel('Wartość funkcji celu (adaptacja)')
plt.legend()
plt.show()


min_values = [min(values) for values in best_values_over_iterations]

print(f"Wartość x dla najlepszego rozwiązania: {best_positions_over_iterations[min_values.index(min(min_values))][0]}")
print(f"Wartość y dla najlepszego rozwiązania: {best_positions_over_iterations[min_values.index(min(min_values))][1]}")
print(f"Średnia wartość funckcji: {sum(min_values) / len(min_values)}")
print(f"Najlepsza wartośc funkcji: {min(min_values)}")
