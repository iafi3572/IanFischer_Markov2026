import numpy as np
import matplotlib.pyplot as plt

sample_size = 10**6

ks = range(2, 11)
ns = [2**k for k in ks]

sample_skew = []
theory_skew = []

for n in ns:
    S = np.random.poisson(lam=n, size=sample_size)
    
    Y = (S - n) / np.sqrt(n)
    
    mu = Y.mean()
    sigma = Y.std()
    
    skew = np.mean((Y - mu)**3) / sigma
    sample_skew.append(skew)
    
    theory_skew.append(1 / np.sqrt(n))

plt.figure()
plt.loglog(ns, sample_skew, 'o', label='Numerical')
plt.loglog(ns, theory_skew, 's', label='Theory: $1/\\sqrt{n}$')
plt.xlabel('n')
plt.ylabel('Skewness S(n)')
plt.legend()
plt.savefig("7e.png")
plt.show()
