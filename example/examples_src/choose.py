import pandas as pd
from sys import argv

filename = argv[1]

df = pd.read_csv(filename, header=None)

print(df.head())
