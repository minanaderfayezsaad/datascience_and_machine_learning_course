import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pandas.read_csv("D:/dr wael data science/digital_marketing_campaign_dataset.csv")



#assignment1--------------------------------------------------------------------------------------------------------------------
"""print("assignment 1")
print("data set")
print(df)

print("top 5 rows******************************")
print(df.head(5))

print("last 5 rows*******************************")
print(df.tail(5))

print("data info***********************")
print(df.info())

print("data shape***************************")
print(df.shape)"""
#end of assignment1--------------------------------------------------------------------------------------------------------------------



#assignment2--------------------------------------------------------------------------------------------------------------------
"""
print("assignment 2")
dataset drawing

x = df["Glucose"]
y = df["Outcome"]

x=np.array([1,2,7,9])
y=np.array([3,8,1,10])

plt.plot(x,y,marker="+")
plt.show()
"""
#end assignment2--------------------------------------------------------------------------------------------------------------------




#assignment3--------------------------------------------------------------------------------------------------------------------
# assigment3 is numpy in file np.py
#end of assignment3--------------------------------------------------------------------------------------------------------------------



#assignment4--------------------------------------------------------------------------------------------------------------------

#print("assignment 4")
#barplot
"""plt.figure(figsize=(10,6))
sns.barplot(x='Gender', y='Conversion', data=df)
plt.title('bar chart')
plt.savefig('conversion_by_gender.png', dpi=300, bbox_inches='tight')
plt.show()
"""

#second barplot
"""plt.figure(figsize=(10,6))
sns.barplot(x='CampaignChannel', y='Conversion', data=df)
plt.title('bar chart')
plt.savefig('conversion_by_CampaignChannel.png', dpi=300, bbox_inches='tight')
plt.show()
"""




#lineplot
"""plt.figure(figsize=(10,6))
sns.lineplot(x='Gender', y='Conversion', data=df,markers='o')
plt.title('line chart')
plt.savefig('linechart_conversion_by_gender.png', dpi=300, bbox_inches='tight')
plt.show()
"""
#second lineplot
"""plt.figure(figsize=(10,6))
sns.lineplot(x='CampaignChannel', y='Conversion', data=df)
plt.title('Line Chart')
plt.savefig('linechart_conversion_by_CampaignChannel.png', dpi=300, bbox_inches='tight')
plt.show()"""


#scatterplot
"""plt.figure(figsize=(10,6))
sns.scatterplot(x='CampaignChannel', y='Conversion', data=df)
plt.title('scatter chart')
plt.savefig('scatterplot_by_CampaignChannel.png', dpi=300, bbox_inches='tight')
plt.show()"""


#boxenplot
"""plt.figure(figsize=(10,6))
sns.boxenplot(x='CampaignChannel', y='Conversion', data=df)
plt.title('boxen chart')
plt.savefig('boxenplot_by_CampaignChannel.png', dpi=300, bbox_inches='tight')
plt.show()"""


#histogram
"""plt.figure(figsize=(10,6))
sns.histplot(df['PreviousPurchases'],bins=5,kde=True)
plt.title('histograph chart')
plt.savefig('histplot_by_Age.png', dpi=300, bbox_inches='tight')
plt.show()"""

