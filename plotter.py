import os
import pandas as pd

for csv in os.scandir('CSVs'):
    table = pd.DataFrame.from_csv(csv.path)
    print(table)