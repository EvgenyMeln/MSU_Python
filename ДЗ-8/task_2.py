import numpy as np

salaries = np.loadtxt('input.txt')

print(f"{np.median(salaries):.2f}", end = ' ')
print(f"{np.mean(salaries):.2f}", end = ' ')
print(f"{np.std(salaries):.2f}")
