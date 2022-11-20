import numpy as np 
a = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]]) 
power = np.linalg.matrix_power(a, 2) 
print(power) 