import numpy as np
import time
import matplotlib.pyplot as plt
def newton(u, max_iter=20, tol=1e-10):
    x = -np.log(1 - u)

    for _ in range(max_iter):
        g  = 1.0 - (x + 1.0) * np.exp(-x) - u
        gp = x * np.exp(-x)
        x_new = x - g / gp
        if x_new <= 0:
            x_new = 1e-8
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x

def partb():
    N = 10**6
    U = np.random.rand(N)
    X = np.empty(N)

    start = time.time()

    for i in range(N):
        X[i] = newton(U[i])

    end = time.time()
    print(f"Inverse Sampling Runtime: {end - start:.2f} seconds")
    plt.hist(X, bins=100, density=True)
    x_vals = np.linspace(0, X.max(), 500)
    pdf_vals = x_vals * np.exp(-x_vals)
    plt.plot(x_vals, pdf_vals)

    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title("Inverse Sampling")
    plt.savefig("p2.png")
    plt.show()


def partc():
    N = 10**6
    c = 4/np.e
    accepted = np.empty(N)
    count = 0
    start = time.time()

    while count < N:
        X = np.random.exponential(scale=2.0)
        u = np.random.rand()

        if u <= (X * np.exp(1 - X/2)) / 2:
            accepted[count] = X
            count += 1

    end = time.time()

    print(f"Acceptance Rejectance Runtime: {end - start:.2f} seconds")

def partd():
    N = 10**6

    start = time.time()
    E1 = np.random.exponential(scale=1.0, size=N)
    E2 = np.random.exponential(scale=1.0, size=N)
    X = E1 + E2
    end = time.time()
    print(f"Gamma Sampling Runtime: {end - start:.4f} seconds")
partb()
partc()
partd()