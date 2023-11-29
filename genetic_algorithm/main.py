from population import Population
import sys

NR_OF_EPOCHS = int(sys.argv[1])
POPULATION_SIZE = int(sys.argv[2])
CROSSOVER_PROBABILITY = float(sys.argv[3])
MUTATION_PROBABILITY = float(sys.argv[4])

best_values = []
population = Population(POPULATION_SIZE, 6404180)
best_individual = 0
population.generate_individuals()
for y in range(5):
    for x in range(NR_OF_EPOCHS):
        population.calculate_adaptation()
        best_individual = population.get_best_individual()
        print(f"Epoch: {x + 1} Best individual weight:"
              f" {best_individual.get_weight()} Best individual val: {best_individual.get_cost()}")
        population.set_probability_in_population()
        population.choose_parents()
        population.generate_children(CROSSOVER_PROBABILITY, MUTATION_PROBABILITY)

best_values.append(best_individual.get_cost())
