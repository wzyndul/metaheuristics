from population import Population

NR_OF_EPOCHS = 100
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.1

population = Population(100, 6404180)
best_individual = 0
population.generate_individuals()
for x in range(NR_OF_EPOCHS):
    population.calculate_adaptation(population.backpack)
    best_individual = population.get_best_individual()
    print(f"Epoch: {x} Best individual weight: {best_individual.get_weight()} Best individual val: {best_individual.get_cost()}")
    population.set_probability_in_population()
    population.generate_individuals()













