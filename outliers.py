import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pandas.read_csv("D:/dr wael data science/digital_marketing_campaign_dataset.csv")

#print(df.describe())

plt.figure(figsize=(10,6))
sns.boxplot(x=df['Income'])
plt.title('boxplot_Income')
plt.show()


outlier = df[(df['Income'] > 150000) | (df['Income'] < 10000)]
print(outlier)
