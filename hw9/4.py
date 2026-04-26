import numpy as np
import matplotlib.pyplot as plt

beta = 1.0
m_vals = np.arange(2, 200)

exact = np.array([np.sum(1/np.arange(1, m)) for m in m_vals])/beta

deterministic = np.log(m_vals) / beta

plt.figure()
plt.plot(m_vals, exact, label=r"$\frac{1}{\beta}\sum_{n=1}^{m-1} \frac{1}{n}$")
plt.plot(m_vals, deterministic, label=r"$\frac{\ln(m)}{\beta}$")
plt.xlabel("m")
plt.ylabel(r"$\tau_m$")
plt.legend()
plt.savefig("4.png")
plt.show()