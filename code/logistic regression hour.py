import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
from scipy.special import expit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams.update({'font.size': 8})

df2 = pd.read_csv('time.csv')
df = pd.DataFrame(df2)

### total incs by state and deaths
total = df.groupby(df['TIMEHR']).size().rename('Counts').reset_index()

lessMed = total[total['Counts'] <= 4232]
moreMed = total[total['Counts'] > 4232]


totalFinal = pd.concat([moreMed, lessMed])
print(totalFinal)

y = np.array([1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
X = totalFinal['TIMEHR'].values.reshape(-1, 1)

# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)

# and plot the result
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(X.ravel(), y, color="black", zorder=20)
X_test = np.linspace(1, 24)

loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color="red", linewidth=3)

ols = LinearRegression()
ols.fit(X, y)
plt.plot(X_test, ols.coef_ * X_test + ols.intercept_, linewidth=1)
plt.axhline(0.5, color=".5")

plt.ylabel("y")
plt.xlabel("X")

plt.legend(
    ("Logistic Regression Model", "Linear Regression Model"),
    loc="lower right",
    fontsize="small",
)
plt.tight_layout()
plt.show()














