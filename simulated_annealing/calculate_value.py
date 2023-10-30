import numpy as np


def function_value(x, function_type): # na przedziale [-150, 150]
    fx = 0
    # - 2 |x + 100| + 10 dla (-105, -95)
    # -2.2 |x - 100| + 11 dla (95, 105)
    # 0 dla x != (-105, -95) lub (95, 105)
    if function_type == "1":
        if -105 < x < -95:
            fx = -2 * np.abs(x + 100) + 10
        elif 95 < x < 105:
            fx = -2.2 * np.abs(x - 100) + 11
        else:
            fx = 0

    elif function_type == "2":  # f(x) = x sin(10PI x) + 1, dla [-1, 2]
        fx = x * np.sin(10 * np.pi * x) + 1
    else:
        print("Podano błędny numer funkcji")
    return fx

