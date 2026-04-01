import math

def fixed_point(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            print(f"Converged in {i+1} iterations")
            return x_new
        
        x = x_new
    
    print("Did not converge")
    return x

f = lambda x: math.exp(2*(x-1))
print(fixed_point(f,1/2))