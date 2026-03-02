import math
import numpy as np
import matplotlib.pyplot as plt

a = 0.04
b = 0.16
K = 0.1
N = 10**6
p = np.zeros(5)
q = np.zeros(5)

for n in range(1, 6):
    if n < 5:
        p[n-1] = K * np.exp(a * n)
    if n > 1:
        q[n-1] = K * np.exp(b * (n-1))

P = np.array([
    [1-p[0], p[0],0,0,0],
    [q[1], 1-p[1]-q[1], p[1],0,0],
    [0,q[2], 1-p[2]-q[2], p[2],0],
    [0,0,q[3], 1-p[3]-q[3], p[3]],
    [0,0,0,q[4], 1-q[4]]
])

# Part a
pi_db = np.zeros(5)
pi_db[0] = 1

for i in range(1,5):
    pi_db[i] = pi_db[i-1] * (p[i-1] / q[i])

pi_db /= np.sum(pi_db)

#Part b
eigvals, eigvecs = np.linalg.eig(P.T)
index = np.argmin(np.abs(eigvals - 1))
vec = eigvecs[:, index]
pi_eig = vec / np.sum(vec)
print(f"Eigenvalue pi approximation:= {pi_eig}")

#Part C
N = 10**6
states = np.zeros(N, dtype=int)
states[0] = 0

for t in range(1, N):
    state = states[t-1]
    states[t] = np.random.choice(5, p=P[state])

counts = np.bincount(states, minlength=5)
dist = counts / N


x = np.arange(1,6)

plt.figure()
plt.bar(x - 0.2, dist, width=0.2)
plt.bar(x,pi_db, width=0.2)
plt.bar(x + 0.2, pi_eig, width=0.2)

plt.xlabel("State")
plt.ylabel("Probability")
plt.title("Comparison of Stationary Distributions")
plt.xticks(x)
plt.legend(["Simulation", "Detailed Balance", "Eigenvector"])
plt.show()


