import pandas as pd

data = pd.read_csv("input.csv")

valid_triangles = data.query('a + b > c and a + c > b and c + b > a')

print(len(valid_triangles))
