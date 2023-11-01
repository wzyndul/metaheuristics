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


def calculate_tick(temperature, k, iterations):
    return temperature / (k * iterations)


# Inicjalizacja początkowych wartości
x_value = random.uniform(LEFT, RIGHT)
x_next = 0
delta_cost = 0
x_best = x_value

for i in range(0, M):
    # tick = calculate_tick(T, K, M)
    x_next = random_neighbour(x_value, 15)
    delta_cost = cal.function_value(x_next, FUNC) - cal.function_value(x_value, FUNC)

    if delta_cost > 0:            # szukanie większej wartości funkcji kosztu
        x_value = x_next
    else:
        x = random.random()       # zwraca losową liczbę z przedziału [0, 1)
        if x < math.exp(-delta_cost / (K * T)):
            x_value = x_next

    T = ALFA_T * T
    if cal.function_value(x_best, FUNC) - cal.function_value(x_value, FUNC) < 0:
        x_best = x_value
        function_val = cal.function_value(x_best, FUNC)
        print(f"Najlepszy punkt: {x_best}, wartość funkcji: {function_val}")
        print(f"Temperatura: {T}")
        print(f"Różnica kosztów rozwiązań: {delta_cost}")
        print(f"Krok: {i}\n")


