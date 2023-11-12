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

def roulette_selection(population, number_selected):
    probability = set_probability_in_population(population)
    sections = []
    summ = 0
    for i in range(0, number_selected):
        sections.append([i, summ, summ + probability[i]])
        summ += probability[i]
    #TODO tutaj slajd 39 dalej implemetacja ale troche nie czaje bo teraz jakby zawsze lecimy od indeksu 0 do n
    # i to nie koniecznie sa najwieksze prawdopodnienstwa a to powinno byc losowanie a nie wybieranie po kolei
def single_point_crossing():
    pass

def even_crossbreedingg():
    pass

def individual_mutation():
    pass
# TODO chyba lepiej obiektowo wszystko machnac niz na tych tablciach leciec


