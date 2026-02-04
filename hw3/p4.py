import numpy as np
import random
P = np.array([
    [1/2, 1/2, 0,   0,   0, 0],
    [0,   1/2, 1/2, 0,   0, 0],
    [1/3, 0,   1/3, 1/3, 0, 0],
    [0,   0,   0,   1/2, 1/2, 0],
    [0,   0,   0,   0,   0, 1],
    [0,   0,   0,   0,   1, 0]
])

n = 10000
rng = np.random.default_rng()

count = 0

for _ in range(n):

    state = 0
    for _ in range(5):
        state = random.choices(range(6), weights=P[state])[0]


    if state == 3:
        count += 1

fraction = count / n
print(f"P(X5 = 4 | X0 = 1): {fraction}")
