import numpy as np
import math 
import matplotlib.pyplot as plt

l = 3

Finv = lambda u: -1/l *  math.ln(u)

def sim_times():
    times = []
    t = 0
    while t<=48:
        t += np.random.exponential(1/l)
        if(t<=48):
            times.append(t)
    return np.array(times)

Atimes = sim_times()
Btimes = sim_times()

plt.eventplot([Atimes, Btimes],
              colors=['red', 'blue'],
              lineoffsets=[1, 0],
              linelengths=0.8)

plt.yticks([0,1], ['Team B', 'Team A'])
plt.xlim(0, 48)
plt.xlabel("Time (minutes)")
plt.title("Basketball Game Simulation ")
plt.savefig("2partc.png")
plt.show()



def sim_times2():
    Atimes = []
    Btimes = []
    t = 0
    while t<=48:
        t += np.random.exponential(1/(2*l))
        if(t<=48):
            U = np.random.choice([0,1])
            if(U):
                Atimes.append(t)
            else:
                Btimes.append(t)
            
    return np.array(Atimes), np.array(Btimes)

Atimes,Btimes = sim_times2()

plt.eventplot([Atimes, Btimes],
              colors=['red', 'blue'],
              lineoffsets=[1, 0],
              linelengths=0.8)

plt.yticks([0,1], ['Team B', 'Team A'])
plt.xlim(0, 48)
plt.xlabel("Time (minutes)")
plt.title("Basketball Game Simulation ")
plt.savefig("2partd.png")

plt.show()




num_games = 10**5

N = np.random.poisson(lam = 2*l*48,size=num_games)
NA = np.random.binomial(n=N, p=0.5)
NB = N-NA
D = 2 * (NA-NB)



E_D = np.mean(D)
Var_D = np.var(D)
P_tie = np.mean(D == 0)

print(f"Estimated E[D]: {E_D}, Theorectical E[D]: 0")
print(f"Estimated Var[D]: {Var_D}, Theorectical Var[D] = {8*l*48}"  )
print(f"Estimated P(D=0): {P_tie}, Theorectical P(D=0): {1/math.sqrt(math.pi * l * 48)} " )



