import csv
import pandas as pd
import numpy as np
# vehicle capacity:
# R1, C1, RC1: 200
# R2, RC2: 1000
# C2: 700

path = 'data/R1/R101.csv'

names = ['id', 'x', 'y', 'demand', 'ready_time', 'due_time', 'service_time']
df = pd.read_csv(path, sep=',', header=None, names=names)
