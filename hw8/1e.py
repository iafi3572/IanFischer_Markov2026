
import numpy as np
import matplotlib.pyplot as plt
import math
Ns = [100,1000,10000,100000]


T =5
def initial():
    return np.random.choice([1,2],p=[1/3,2/3])

def simOne():
    state = initial()
    t = 0

    times = [0]
    states = [state]
    while(t<=T):
        wait= np.random.exponential(1)
        t+= wait
        if(t>T):
            break
        state = (state +1) %4
        times.append(t)
        states.append(state)
    return times,states

def compute_f(N, tvals):
    count_state1 = np.zeros(len(tvals))
    
    for _ in range(N):
        times, states = simOne()
        idx = 0
        current_state = states[0]
        
        for i, t in enumerate(tvals):
            while idx+1 < len(times) and t >= times[idx+1]:
               
                idx += 1
                current_state = states[idx]
            
            if current_state == 1:
                count_state1[i] += 1
        
    f = count_state1 / N
    return  f


 

def f(t):
    return (1/12) * math.exp(-2*t) * (
        3 * math.exp(2*t)
        - 4 * math.exp(t) * math.sin(t)
        + 2 * math.exp(t) * math.cos(t)
        - 1
    )

tvals = np.linspace(0,5,200)
plt.figure()
plt.xlim(0,5)
plt.ylim(0,1/2)
fvals = [f(t) for t in tvals]
plt.plot(tvals,fvals, label = "Theoretical f(t)")
for N in Ns:
    f= compute_f(N,tvals)
    plt.plot(tvals,f, label = f"N ={N}")
plt.legend()
plt.xlabel("t")
plt.ylabel("f(t)")
plt.savefig("1e.png")
plt.show()
       