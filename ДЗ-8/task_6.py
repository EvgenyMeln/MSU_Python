import numpy as np

results = np.genfromtxt('input.csv', delimiter = ',', dtype = int)

means = np.mean(results, axis = 0)

for i in range(len(means)):
    results[0][i] = int(1.5 * means[i])

np.savetxt('output.csv', results, fmt = "%g", delimiter = ',')
