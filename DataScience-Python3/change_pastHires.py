import pandas as pd
import numpy as np
#%%

df = pd.read_csv('PastHires.csv')

df['Hired'].where(df['Hired'] == 'Y', 0, inplace=True)
df['Hired'].where(df['Hired'] == 0, 'N', inplace=True)
df['Hired'].where(df['Hired'] == 'N', 'Y', inplace=True)

#%%

df.to_csv('PastHires_alternate_universe.csv', index=False)
