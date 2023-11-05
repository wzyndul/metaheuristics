import random
import numpy as np
import calculate_value as cal
import sys

# Wczytywanie parametrów z linii poleceń
T = float(sys.argv[1])  # temperatura początkowa
ALFA_T = float(sys.argv[2])  # współczynnik zmiany temperatury
K = float(sys.argv[3])  # stała Boltzmanna
M = int(sys.argv[4])  # liczba iteracji
LEFT = float(sys.argv[5])  # lewa granica przedziału
RIGHT = float(sys.argv[6])  # prawa granica przedziału
FUNC = sys.argv[7]  # numer funkcji


# lsoowanie sąsiada
def random_neighbour(x):
    return random.uniform(max(LEFT, x - 2 * T), min(RIGHT, x + 2 * T))


# Inicjalizacja początkowych wartości
x_value = random.uniform(LEFT, RIGHT)
x_next = 0
delta_cost = 0
x_best = x_value
nr = 0

for i in range(0, M):
    x_next = random_neighbour(x_value)
    delta_cost = cal.function_value(x_next, FUNC) - cal.function_value(x_value, FUNC)

    if delta_cost > 0:  # szukanie większej wartości funkcji kosztu
        x_value = x_next
    else:
        if random.random() < np.exp(-delta_cost / (K * T)):
            x_value = x_next

    if cal.function_value(x_best, FUNC) - cal.function_value(x_value, FUNC) < 0:
        nr += 1
        x_best = x_value
        function_val = cal.function_value(x_best, FUNC)
    T *= ALFA_T
print(f"Najlepszy punkt: {x_best}, wartość funkcji: {function_val}")
print(f"Temperatura: {T}")
print(f"Różnica kosztów rozwiązań: {delta_cost}")
print(f"Iteracja: {i}")
print(f"Liczba poprawek: {nr}\n")