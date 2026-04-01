import numpy as np
import matplotlib.pyplot as plt

X0 = 2
q0 = np.array([0,0,1,0,0])
p = np.array( [[0 , 1 , 0 , 0 , 0 ],
               [1/3 , 0 , 2/3 , 0 , 0 ],
                [0 , 1/2 , 0 , 1/2 , 0 ],
                [0 , 0 , 2/3 , 0 , 1/3 ],
                [0 , 0 , 0 , 1 , 0 ]])

p50 = np.linalg.matrix_power(p,50)
pi = np.array([ 1/12 ,  1/4  , 1/3 , 1/4 , 1/12 ])
q50 = q0 @ p50
i = range(0,5)

plt.plot(i,q50, label = "$q_{50}$")
plt.plot(i,pi, label = "$\pi$")
plt.legend()
plt.xlabel("i")
plt.title("$q_{50}$ and $\pi$")
plt.savefig("1d.png")
plt.show()

print(q50)
print(pi)






