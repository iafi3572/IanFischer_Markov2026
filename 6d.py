from numpy import random

N = 10**5


def sim():
    Xn=1 
    S = 0
    for _ in range(200):
        S += Xn
        Xn = 2*random.binomial(n=Xn, p=1/2)
        if(Xn ==0):
            return S
    return 0

S = [sim() for _ in range(N)]

print(f"Simulated N={N}: {S.count(3)/N}")
print(f"Exact : {1/8}")
 