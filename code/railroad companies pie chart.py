import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})

df2 = pd.read_csv('2010_2021_changedStates.csv')
df = pd.DataFrame(df2)

total = df.groupby(df['RAILROAD']).size().rename('Counts').reset_index()

total2 = total.sort_values('Counts', ascending=False).head()

labels = total2['RAILROAD']
sizes = total2['Counts']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()
