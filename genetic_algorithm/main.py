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
        print(f"Epoch: {x + 1} Best individual weight:"
              f" {best_individual.get_weight()} Best individual val: {best_individual.get_cost()}")
        population.set_probability_in_population()
        population.choose_parents()
        population.generate_children(CROSSOVER_PROBABILITY, MUTATION_PROBABILITY)

    best_values.append(best_individual.get_cost())

plt.plot(list(range(1, 6)), best_values, marker='o')
plt.xlabel('Run')
plt.ylabel('Best individual value')
plt.title('Best individual values for 5 runs')
plt.xticks(list(range(1,6)))
plt.grid(True)
plt.show()