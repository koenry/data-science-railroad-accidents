import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("2010_2021_changedStates.csv")

meanAge = []
medianAge = []

yearList = [*range(2010, 2022, 1)]
print(yearList)
for w in yearList:
    a = df.loc[(df['YEAR4'] == w).dropna()]
    
    meanAge.append(a['AGE'].median())
    medianAge.append(round(a['AGE'].mean(), 1))
   
labels = yearList
meanAge2 = meanAge
medianAge2 = medianAge

x = np.arange(len(labels)) 
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, meanAge2, width, label='Mean')
rects2 = ax.bar(x + width/2, medianAge2, width, label='Median')

ax.set_ylabel('Age')
ax.set_title('Median and Mean age of accidents 2010-2021 year')
ax.set_xticks(x, labels)
ax.legend(loc='lower right')

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()
