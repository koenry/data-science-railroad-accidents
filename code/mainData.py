import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 8})

df2 = pd.read_csv('2010_2021_updated.csv')
df = pd.DataFrame(df2)
df = df[df.columns]

### total incs by state and deaths
inc = df.groupby(df[ 'STATE']).size().rename('Counts').reset_index()

deaths = df.loc[(df['CASFATAL'] == 'Y')]
deaths2 = df.groupby(deaths['STATE']).size().rename('Counts').reset_index()

x3 = np.array(deaths2['STATE'])
y3 = np.array(deaths2['Counts'])

x4 = np.array(inc['STATE'])
y4 = np.array(inc['Counts'])
y_pos = range(len(x3))
plt.bar(y_pos, y3)
plt.xticks(y_pos, x3, rotation=90, )
plt.title('Total railroad  Deaths by state 2010-2021')
plt.savefig(f'Deaths 1.png')
plt.show()

y_pos = range(len(x4))
plt.bar(y_pos, y4)
plt.xticks(y_pos, x4, rotation=90, )
plt.title('Total railroad accidents by state 2010-2021')
plt.savefig(f'Total 2.png')
plt.show()
### total incs and death toll by year and state 

yearsArray = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
for w in yearsArray:
    dths = df.loc[(df['YEAR4'] == w) & (df['CASFATAL'] == 'Y')]
    stateNDe = df.groupby(dths['STATE']).size().rename('Counts').reset_index()

    total = df.loc[(df['YEAR4'] == w) & (df['CASFATAL'] == 'N')]
    totalState = df.groupby(total['STATE']).size().rename('Counts').reset_index()

    x = np.array(stateNDe['STATE'])
    y = np.array(stateNDe['Counts'])

    x2 = np.array(totalState['STATE'])
    y2 = np.array(totalState['Counts'])

    y_pos = range(len(x2))
    plt.bar(y_pos, y2)
    plt.xticks(y_pos, x2, rotation=90)
    
    plt.title(f'Total railroad accidents by state in {w}')
    plt.savefig(f'Total {w}.png')
    plt.show()
    
    y_pos = range(len(x))
    plt.bar(y_pos, y)
    plt.xticks(y_pos, x, rotation=90)
    
    plt.title(f'Total railroad casualties by state {w}')
    plt.savefig(f'Deaths {w}.png')
    plt.show()
#############################################################################







