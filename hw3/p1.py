import numpy as np
import matplotlib.pyplot as plt

a = np.sqrt(3) - 1
c = np.exp(-a) / (3 * a**2 * (1 - a))

x = np.linspace(0, 15, 500)
f = (1/3) * x * (1 + x) * np.exp(-x)
cg = c * (a**2) * x * np.exp(-a * x)

plt.plot(x, cg, 'r--', label=r'$c(a)g_a(x)$')
plt.plot(x, f, 'b-', label=r'$f(x)$')
plt.legend()
plt.savefig("p1.png")
plt.show()