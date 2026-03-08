import numpy as np
import matplotlib.pyplot as plt

a = 0.99
P = np.array([[1-a,a,0],
              [a,0,1-a],
              [0,1-a,a]])

def sim(N,x0=1,t=300): 
    '''
    Inputs: 
        N - number of sims
        x0 - initial state (1,2,3)
        t - how long to run sims
    Outputs: 
        fn - array with the ith entry being the fraction of chains in state 1 at time i
    '''
    state = x0
    states = [1,2,3]
    currentstates = [x0] * N 
    fn = [0] * t
    
    for n in range(t):
        fn[n] = currentstates.count(1)/N
        
        for i in range(N):
            currentstates[i] =  np.random.choice(states, p=P[currentstates[i]-1])
    return fn

def plotter(fn,N,t=300):
    cs = np.array([1/3, 0.00253153, -0.335865 ])
    lambdas = [1,-0.983038, 0.985038] 
    vs1  = [1,196.504,-.503807] 
    qn1 = [0] * t
    for i in range(t):
        qn1[i] = cs[0] * vs1[0] * lambdas[0]** i+ cs[1] * vs1[1] * lambdas[1]** i + cs[2] * vs1[2] * lambdas[2]** i
    xs = np.arange(t)

    plt.figure()
    plt.plot(xs, qn1, label="Theoretical $q_n(1)$")
    plt.plot(xs, fn, label="Simulated $f_n$")
    plt.xlabel("n")
    plt.ylabel("Fraction of Chains at state 1")
    plt.title(f"Simulated and Theoretical # of Markov Chains at State 1 for N={N}")
    plt.legend()
    plt.savefig(f"plotN{N}.png")
    plt.show()
    
plotter(sim(100),100)
plotter(sim(1000),1000)
plotter(sim(10000),10000)