import numpy as np

a,b = 1,1
L = 20
N = 1500

times = []
for _ in range(N):
    i =0 
    t= 0.0
    while(i< L):
        if i == 0:
            rate = a
            t += np.random.exponential(1 / rate)
            i += 1
        
        else:
            rate = a + b
            t += np.random.exponential(1 / rate)

            if np.random.rand() < a / rate:
                i += 1
            else:
                i -= 1
    times.append(t)
times = np.array(times)

mean = np.mean(times)
variance = np.var(times)

print(f"Theretical m0 {(L*(L+1))/(2*a)}")
print(f"Estimated m0 for N = {N}: {mean}")
print(f"Simulated variance: {variance}")