import numpy as np
import matplotlib.pyplot as plt

X0 = 2
q0 = np.array([0,0,1,0,0,0])
p = np.array([ [0    , 2/3  , 0    , 1/3  , 0    , 0  ],
           [1/3  , 0    , 1/3  , 1/3  , 0    , 0  ],
           [0    , 1/2  , 0    , 0    , 1/2  , 0  ],
           [1/5  , 2/5  , 0    , 0    , 2/5  , 0  ],
           [0    , 0    , 1/3  , 1/3  , 0    , 1/3  ],
          [0    , 0    , 0    , 0    , 1    , 0  ]])

p50 = np.linalg.matrix_power(p,50)
pi = np.array([ 3/26 ,  3/13  , 2/13 , 5/26 , 3/13,1/13 ])
q50 = q0 @ p50
i = range(0,6)

plt.plot(i,q50)
plt.plot(i,pi)
plt.show()

print(q50)
print(pi)






