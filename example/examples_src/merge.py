import pandas as pd
from sys import argv

output_name = argv[1]
for filename in argv[2:]:
    df = pd.read_csv(filename, header=1)
    df.to_csv(output_name, mode='a', index=False, header=0)
