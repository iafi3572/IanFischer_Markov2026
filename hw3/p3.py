import numpy as np
p = np.array([
    [1.0, 0.0, 0.0, 0.0, 0.0],    
    [1/3, 0.0, 2/3, 0.0,0.0], 
    [0.0, 1/3, 0.0, 2/3, 0],
    [0.0,0.0,1/3,0.0,2/3],
    [0.0,0.0,0.0,0.0,1]     
])

p_4 = np.linalg.matrix_power(p, 4).round(3)

print("\\[p^4=\\begin{pmatrix}")
for row in p_4:
    print("\\\\")
    for ele in row:
        print(ele, end=" & ")
print("\\end{pmatrix}\\]")
print() 
print("p^4")
print(p_4)