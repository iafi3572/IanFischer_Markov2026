
import math 

def f(N):
    g   =  lambda n:(2/3)**n * 1/ math.factorial(n)
    s = 0
    for n in range(N):
        s+= g(n)
    return g(N)* 1/s

for N in range(1,100):
    if(f(N) < .02):
        print(N)
        break