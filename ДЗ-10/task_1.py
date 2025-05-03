import pandas as pd

data = pd.read_csv("input.csv")

data.dropna(subset=['name'], inplace = True)
mean = data.score.mean()
data.fillna(mean, inplace = True)

data.to_csv('output.csv', index = True)
