from population import Population
import matplotlib.pyplot as plt
import sys

NR_OF_EPOCHS = int(sys.argv[1])
POPULATION_SIZE = int(sys.argv[2])
CROSSOVER_PROBABILITY = float(sys.argv[3])
MUTATION_PROBABILITY = float(sys.argv[4])

best_values = []
for y in range(5):
    population = Population(POPULATION_SIZE, 6404180)
    best_individual = 0
    population.generate_individuals()
    for x in range(NR_OF_EPOCHS):
        population.calculate_adaptation()
        best_individual = population.get_best_individual()
        population.set_probability_in_population()
        population.choose_parents()
        population.generate_children(CROSSOVER_PROBABILITY, MUTATION_PROBABILITY)

    best_values.append(best_individual.get_cost())


mean_value = sum(best_values) / len(best_values)
for i in range(5):
    print(f'Run {i + 1}: {best_values[i]}')

print("mean value: ", mean_value)

fig, ax = plt.subplots()
ax.plot(list(range(1, 6)), best_values, marker='o', label='Best individual')
ax.axhline(y=mean_value, color='red', linestyle='--', label='Mean value')

ax.set_xlabel('Run')
ax.set_ylabel('Best individual value')
ax.set_title('Best individual values for 5 runs')
ax.set_xticks(list(range(1, 6)))
ax.grid(True)
ax.legend()

plt.show()