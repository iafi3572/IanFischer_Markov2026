import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.integrate import quad

f = lambda u: (u**4)/(u**6 +1)
x = np.arange(1,5.1,.1)
N = [int(np.floor(10**i)) for i in x]
E = []
for n in N:
    count = 0
    for _ in range(n):
        u, v = random.random(), random.random()
        if v < f(u):
            count += 1
    E.append(count / n)

true_value = quad(f, 0, 1)[0]

plt.semilogx(N, E, label="Monte Carlo estimate")
plt.axhline(true_value, color='r', linestyle='--', label="Integral Value")
plt.xlabel("N")
plt.ylabel("Integral estimate")
plt.legend()
plt.savefig("3b.png", dpi=300, bbox_inches="tight")

 




