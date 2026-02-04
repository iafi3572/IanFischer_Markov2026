import numpy as np
p = np.array([
    [1.0, 0.0, 0.0, 0.0, 0.0],    
    [1/3, 0.0, 2/3, 0.0,0.0], 
    [0.0, 1/3, 0.6]     
])

p_50 = np.linalg.matrix_power(p, 50)
print("p^50")
print(p_50)