import numpy as np 
a = np.matrix('1 2 2; 2 1 -2; 2 -2 1') 
a_inv = np.linalg.inv(a) 
print(a_inv) 