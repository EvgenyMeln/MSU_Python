import numpy as np

salaries = np.genfromtxt('input.csv', delimiter = ',', dtype = float)

salaries[0::2, 1::2] /= 2 
salaries[1::2, 0::2] /= 2

np.savetxt('output.csv', salaries, fmt = "%g", delimiter = ',')
