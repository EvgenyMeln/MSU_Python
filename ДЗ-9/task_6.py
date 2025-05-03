import pandas as pd

data = pd.read_csv("input.csv")
sums = data.sum()
index_of_best = sums.values.argmax()

if sum(sums.values) >= 8000000:
    print("1", sums.index[index_of_best])
else:
    print("0", sums.index[index_of_best])



