import numpy as np
import math
import matplotlib.pyplot as plt

# when to truncate
N = 10

def poisson(l):
    return lambda x: math.exp(-l) *  l**x/math.factorial(x)

# part a
pX_a = poisson(2) 
pX_b = poisson(1.5) 


pAwins = 0
for i in range(N+1):
    subtotal = 0
    for j in range(i):
        subtotal += pX_b(j)
    pAwins += pX_a(i) * subtotal

print(f"Probability Team A wins: {pAwins}")

# part b
A = lambda t: poisson(2-2/90 * t)
B = lambda t: poisson(1.5-1.5/90 * t)
tvals = np.arange(0,91,1)
pTieVals = []

for t in tvals:
    pTie = 0
    for i in range(N+1):
        pTie += A(t)(i) * B(t)(i)
    pTieVals.append(pTie)

plt.plot(tvals,pTieVals)
plt.savefig("1partb.png")
plt.show()


#part c
pTieVals2 = []
for t in tvals:
    pTie = 0
    if t < 60:
        for i in range(N+1):
            pTie += A(t)(i) * B(t)(i)
    else:
        for i in range(N+1):
            pTie += A(t)(i) * B(t)(i+1)
    
    pTieVals2.append(pTie)

plt.plot(tvals, pTieVals2)
plt.savefig("1partc.png")

plt.show()


