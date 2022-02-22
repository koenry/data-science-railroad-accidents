import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("2010_2021_changedStates.csv")

text2 = " ".join(RAILROAD for RAILROAD in df.RAILROAD)

word_cloud2 = WordCloud(collocations = False, background_color = 'black').generate(text2)

plt.imshow(word_cloud2, interpolation='bilinear')
plt.axis("off")
plt.show()
