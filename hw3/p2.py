import numpy as np
import random
def parte():
    p = np.array([
        [0.9, 0.1, 0.0],    
        [0.0, 0.875, 0.125], 
        [0.4, 0.0, 0.6]     
    ])

    p_50 = np.linalg.matrix_power(p, 50).round(3)
    print("p^50")
    print(p_50)

def partf():

    def oneRound(currentState):
        U = random.random()
        if currentState == 'G':
            if(U<1/10):
                return 'S'
            else:
                return 'G'
        elif currentState == 'S':
            if(U<1/8):
                return 'D'
            else:
                return 'S'
        else:
            if(U<2/5):
                return 'G'
            else:
                return 'D'
    n = 10000
    lst = []
    state= 'G'
    for _ in range(n):
        lst.append(state)
        state = oneRound(state)
    print(lst.count('G')/len(lst))
    return lst.count('G')/len(lst)
partf()