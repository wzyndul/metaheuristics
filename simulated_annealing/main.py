import math

import numpy as np
import random
import calculate_value as cal

# TODO dodac ograniczenie zeby nie wyjsc poza przedzial
def random_neighbour(x, tick): # na sztywno na razie
    change = random.uniform(-tick, tick)
    if x + change > 150 or x + change < - 150:
        return x - change
    else:
        return x + change
# na razie na sztywno wszystko, numery funkcji i przedziały itd wziete z tego pdfa
# 1 funckaj to na przedziale [-150, 150]
# a funkcja 2 to ta z sinusem i na przedziale [-1, 2]


# 1. inicjalizacja początkowej wartości
# myslę, że może to być losowanie po prostu x z zakresu na jakim sprawdzamy funkcje

x_value = random.uniform(-150, 150)
x_next = 0

# 2. inicjalizacja temperatury
# to raczej trzeba bedzie po prostu dobrac i poeksperymentowac
t = 500
k=0.1

# 3. kryterium stopu, z zadania się weźmie (mozna podac po prostu)
stop = 3000

delta_cost = 0

x_best = x_value

for i in range(0, stop):
    x_next = random_neighbour(x_value, 15)
    delta_cost = cal.function_value(x_next, "1") - cal.function_value(x_value, "1") # na sztywno 1 funckja na razie wszedzie
    if delta_cost > 0: # szukam wiekszej wartoscci funkcji kosztu
        x_value = x_next
    else:
        x = random.random() # returns random float between 0 and 1
        if x < math.exp(-delta_cost / (k * t)):
            x_value = x_next
    t = 0.999*t
    if cal.function_value(x_best, "1") - cal.function_value(x_value, "1") < 0:
        x_best = x_value
        print(x_best)


