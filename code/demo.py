import pandas as pd
import numpy as np

df2 = pd.read_csv('2010_2021_updated.csv')
df = pd.DataFrame(df2)
df = df[df.columns]
df2 = df.head(1000)

df2.to_csv('demo.csv', index=False)
