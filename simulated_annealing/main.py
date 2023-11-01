import math
import random
import calculate_value as cal
import sys

# Wczytywanie parametrów z linii poleceń
T = float(sys.argv[1])          # temperatura początkowa
ALFA_T = float(sys.argv[2])     # współczynnik zmiany temperatury
K = float(sys.argv[3])          # stała Boltzmanna
M = int(sys.argv[4])            # liczba iteracji
LEFT = float(sys.argv[5])       # lewa granica przedziału
RIGHT = float(sys.argv[6])      # prawa granica przedziału
FUNC = sys.argv[7]              # numer funkcji

# def random_neighbour(x, tick):
#     change = random.uniform(-tick, tick)
#     if x + change > RIGHT or x + change < LEFT:
#         return x - change
#     else:
#         return x + change


def random_neighbour(x, tick):
    change = random.uniform(-tick, tick)
    x_neighbor = x + change

    # Sprawdzanie czy punkt nie wychodzi poza przedział
    x_neighbor = max(min(x_neighbor, RIGHT), LEFT)
    return x_neighbor


def calculate_tick(initial_temperature, final_temperature, iterations):
    return (initial_temperature - final_temperature) / iterations


# 1. inicjalizacja początkowej wartości

x_value = random.uniform(LEFT, RIGHT)
x_next = 0

# 2. inicjalizacja temperatury to trzeba dobrac (podaje sie w parametrach skryptu)
# wartosc k tez sie podaje w parametrach


# 3. kryterium stopu, z zadania się weźmie (mozna podac po prostu) - w parametrach

delta_cost = 0
x_best = x_value
curr_T = T

for i in range(0, M):
    x_next = random_neighbour(x_value, 15)
    delta_cost = cal.function_value(x_next, FUNC) - cal.function_value(x_value, FUNC)
    if delta_cost > 0: # szukam wiekszej wartoscci funkcji kosztu
        x_value = x_next
    else:
        x = random.random() # returns random float between 0 and 1
        if x < math.exp(-delta_cost / (K * T)):
            x_value = x_next
    T = ALFA_T * T
    if cal.function_value(x_best, FUNC) - cal.function_value(x_value, FUNC) < 0:
        x_best = x_value
        print(x_best)


