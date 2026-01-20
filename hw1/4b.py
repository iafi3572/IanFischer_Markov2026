import random
import matplotlib.pyplot as plt
import numpy as np

N = 10**5
tvals = np.linspace(0,1)
def f(t):
    return 3*t**2

Tvals = []
for _ in range(N):
    M = random.random()
    A = random.random()
    D = random.random()
    T = max(M,A,D)
    Tvals.append(T)

plt.plot(tvals,f(tvals))
plt.hist(Tvals, bins=50, density=True, range=(0,1), alpha=0.6)
plt.xlabel("Time after 6PM (hours)")
plt.ylabel("PDF")
plt.legend(["Theoretical PDF", "Simulation"])
plt.savefig("4b.png", dpi=300, bbox_inches="tight")

plt.show()
