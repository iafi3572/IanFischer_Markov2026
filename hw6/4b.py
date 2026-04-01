from numpy import random

a = 0.49
N = 10**5


def sim():
    Xn=1 
    for _ in range(200):
        Xn = 2*random.binomial(n=Xn, p=1-a)
        if(Xn ==0):
            return 1
        
    return 0

count = 0
for _ in range(N):
    count += sim()

print(f"Simulated N={N}: {count/N}")
print(f"Expected: {a/(1-a)}") 