import random

BACKPACK = [(1,3), (2,4)] # (weight, cost)
MAX_WEIGHT = 9
def calculate_adaptation(individual): # backacp i max weight jako stałe jakies zrobie na razie
    weight = 0                                              # najwyzej sie to obiektowo potem zrobi
    cost = 0
    for index, value in individual:
        if value == 1:
            weight += BACKPACK[index][0]
            cost += BACKPACK[index][1]
    if weight > MAX_WEIGHT:
        return 0
    else:
        return weight


def generate_initial_population(population_size, individual_size):
    population = []
    for x in range(population_size):
        individual = []
        for y in range(individual_size):
            individual.append(random.choice([0, 1]))
        population.append(individual)
    return population


def set_probability_in_population(population):
    adaptation_sum = 0
    probability = []
    for individual in population:
        adaptation_sum += calculate_adaptation(individual)
    for individual in population:
        probability.append(calculate_adaptation(individual)/adaptation_sum)
    return probability


def roulette_selection(population, number_of_parents):
    probability = set_probability_in_population(population)
    sections = []
    summ = 0

    # Tworzymy przedziały dla każdego osobnika w populacji
    for i in range(len(population)):
        sections.append([i, summ, summ + probability[i]])
        summ += probability[i]

    chosen_individuals = []

    # Wybieramy osobniki na podstawie ruletki
    for _ in range(number_of_parents):
        random_numer = random.uniform(0, 1)
        for section in sections:
            if section[1] < random_numer <= section[2]:
                chosen_individuals.append(population.pop([section[0]]))
                # robie popa, zeby usunac z popualcji tego osobniak, zeby przypadkiem nei wybrac go dwa razy w metodzie ruletki
                #TODO still nie wiem do konca jak chce zrobic to wybieranie rodzicow w sensie ilu ich itd
                # TODO ale chyba po prostu krzyzowanie i powstaje po 2 dzieci i gitara jest

                break

    return chosen_individuals

#todo pamietaj o tym!!!!
# Jeśli prawdopodobieństwo krzyżowania wynosi 1.0, to krzyżowanie będzie miało miejsce za każdym razem podczas
# tworzenia potomstwa. Z drugiej strony, jeśli prawdopodobieństwo krzyżowania wynosi 0.0,
# to krzyżowanie nie będzie miało miejsca, a potomstwo będzie identyczne z rodzicami.
def single_point_crossing(parent_a, parent_b, crossover_probability):
    if random.random() < crossover_probability:
        children_a, children_b = [], []
        crossing_point = random.randint(1, 7) # wykluczamy wybranie wszystkich genów z 1 rodzica, 7 bo i tak jest to excluded w rangu
        for index in range(0, crossing_point):
            children_a.append(parent_a[index])
            children_b.append(parent_b[index])
        for index in range(crossing_point, len(parent_a)):
            children_a.append(parent_b[index])
            children_b.append(parent_a[index])
        return children_a, children_b
    else:
        return parent_a, parent_b # dzieci są takie same jak rodzice


def two_point_crossing(parent_a, parent_b, crossover_probability):
    if random.random() < crossover_probability:
        children_a, children_b = [], []
        while True:
            number1 = random.randint(1, 7)
            number2 = random.randint(1, 7)
            if number1 != number2 and abs(number1 - number2) > 2: # liczby nie mogą być identyczne ani 2 miejsca od siebie (bo excluded) weic de facto 1 miejsce
                break
        for index in range(0, min(number1, number2)):
            children_a.append(parent_a[index])
            children_b.append(parent_b[index])

        for index in range(min(number1, number2), max(number1, number2)):
            children_a.append(parent_b[index])
            children_b.append(parent_a[index])

        for index in range(max(number1, number2), len(parent_a)):
            children_a.append(parent_a[index])
            children_b.append(parent_b[index])

        return children_a, children_b
    else:
        return parent_a, parent_b  # dzieci są takie same jak rodzice

def individual_mutation():
    pass


