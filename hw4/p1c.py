import random
import math

q= 0.4
p=0.35
s=0.25
i=10
N = 100000
random.seed(42)
def play(i):
    if(i==0):
        return 0
    else: 
        U = random.random()
        if(U<q):
            return play(i-1)
        elif(U<p+q):
            return play(i+1)
        else:
            return i

total =0
for _ in range(N):
    total += play(10)

e10 =  (p-q)/(s) *  (1-(((1 -math.sqrt(1-4*p*q))/(2*p) ))**10) +10
print(f"Numerical Expected Value: {total/N}") 
print(f"Theorectical Expected Value: {e10}")


