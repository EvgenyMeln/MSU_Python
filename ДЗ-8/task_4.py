import numpy as np

count = np.genfromtxt('input.csv', delimiter = ',', dtype = int)

sums = np.sum(count, axis = 0)

print(np.argmax(sums) + 1)
