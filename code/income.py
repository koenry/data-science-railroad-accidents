import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

### income dataset
df2Second = pd.read_csv('income.csv')
dfSecond = pd.DataFrame(df2Second)

# get row median by 2010-2020
medianIncome = dfSecond.iloc[:, [2, 3, 4 ,5 ,6 ,7 ,8, 9, 10, 11, 12  ]].median(axis=1)
dfSecond['Median'] = medianIncome

# railroad dataset
df2 = pd.read_csv('2010_2021_updated.csv')
df = pd.DataFrame(df2)
# remove 2021 we dont have the population or income data for 2021
df = df[df['YEAR4']!=2021] 

x2 = df.groupby(df['STATE']).size().rename('Counts').reset_index()

x3 = dfSecond[['Median']].dropna().values.reshape(-1, 1)
x3Train = dfSecond[['Median']].dropna().values.reshape(-1, 1)

y3 = x2['Counts'].values.reshape(-1, 1)
y3Train =  x2['Counts'].values.reshape(-1, 1)

# prepare the model
regr = linear_model.LinearRegression()
regr.fit(x3Train, y3Train)
yPred = regr.predict(x3)

# plot
plt.scatter(y3, x3, color="red")
plt.plot(yPred, x3, color="blue", linewidth=1)
plt.xlabel("Total Railroad accidents 2010-2020 by state")
plt.ylabel("Median 2010-2020 Income by State")
plt.xticks((0, 1500, 5000, 10000, 15000, 20000))
plt.yticks((35000, 50000, 70000))
plt.show()









