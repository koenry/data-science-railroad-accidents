import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 8})

df2 = pd.read_csv('time.csv')
df = pd.DataFrame(df2)

total = df.groupby(df['TIMEHR']).size().rename('Counts').reset_index()

x = total['TIMEHR']
y = total['Counts']

plt.xlabel('Hour')
plt.ylabel('Accident count')
plt.stem(x, y)
plt.show()
