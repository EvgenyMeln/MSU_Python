import pandas as pd

data = pd.read_csv("input.csv")
means = data.mean()
index_of_best = data.mean().values.argmax()

print(means.index[index_of_best])

