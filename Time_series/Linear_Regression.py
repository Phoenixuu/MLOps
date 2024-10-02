import pandas as pd

df = pd.read_csv("/home/dunggps/Code_đảo_điên/MLOps/MLOps/Time_series/book_sales.csv",
                index_col ='Date',
                parse_dates=['Date'],
                ).drop('Paperback', axis = 1)
print(df.head())

import numpy as np

df['Time'] = np.arange(len(df.index))

print(df.head())
