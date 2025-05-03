import pandas as pd

data = pd.read_csv("input.csv", dtype = {"date": str})

data["temperature_f"] = round((data["temperature_c"] * 9/5) + 32)

data = data[["date", "temperature_c", "temperature_f"]]

data.to_csv('output.csv', index = True)
