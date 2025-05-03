import pandas as pd
import numpy as np

data = pd.read_csv("input.csv")
average_hits = data.mean().values

print(np.argmin(average_hits) + 1)

    
    
    
