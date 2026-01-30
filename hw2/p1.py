import numpy as np
import matplotlib.pyplot as plt

gamma = 4 
x0 = 10
Ns = [100,1000,10000]

x = np.linspace(x0, 60, 1000)
C = (gamma - 1) * x0**(gamma - 1)
pdf = C * x**(-gamma)

def sample(N, gamma, x0):
    u = np.random.rand(N)
    return x0 * (1 - u)**(-1 / (gamma - 1))

for N in Ns:
    samples = sample(N, gamma, x0)
    
    plt.figure()
    plt.hist(samples, bins=50, range=(0, 60), density=True)
    plt.plot(x, pdf)
    plt.xlim(0, 60)
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title(f"Power-law samples (N = {N})")
    plt.savefig(f'p1.{N}.png')
    plt.show()