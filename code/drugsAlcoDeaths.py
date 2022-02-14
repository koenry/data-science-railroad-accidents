import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df2 = pd.read_csv('2010_2021_changedStates.csv')
df = pd.DataFrame(df2)
df = df[df.columns]

# deaths
a = df.loc[(df['CASFATAL'] == 'Y')]
totalDeaths = df.groupby(a['CASFATAL']).size().rename('Counts').reset_index()


### alcohol
alco = df.groupby(df['ALCOHOL']).size().rename('Counts').reset_index()
alcoCount = alco['Counts'][2] + alco['Counts'][3]

alcoDeath = df.groupby(a['ALCOHOL']).size().rename('Counts').reset_index()
alcoDeath2 = alcoDeath['Counts'][2]


### drugs
drug = df.groupby(df['DRUG']).size().rename('Counts').reset_index()
drugCount = drug['Counts'][2] + drug['Counts'][3] + drug['Counts'][4]

drugDeath = df.groupby(a['DRUG']).size().rename('Counts').reset_index()
drugDeath2 = drugDeath['Counts'][2] + drugDeath['Counts'][3]


y = [alcoDeath2, totalDeaths['Counts'], drugDeath2]
mylabels = ["Alcohol", "Other", "Drug"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()
