import numpy as np

count = np.zeros(2)
counts = np.genfromtxt('input.csv', delimiter = ',')

for row in counts:
    if -4 <= np.std(row) <= 4:
        count[0] += 1 
    else:
        count[1] += 1

print(np.argmax(count) + 1)
