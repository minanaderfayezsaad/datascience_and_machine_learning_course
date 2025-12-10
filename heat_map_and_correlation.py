import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pandas.read_csv("D:/dr wael data science/digital_marketing_campaign_dataset.csv")


"""x=np.array([1,2,7,9])
y=np.array([3,8,1,10])

plt.plot(x,y,marker="+")
plt.show()"""

#assignment5--------------------------------------------------------------------------------------------------------------------
numeric_df = df[[
    'Age', 'Income', 'AdSpend', 'ClickThroughRate', 'ConversionRate',
    'WebsiteVisits', 'PagesPerVisit', 'TimeOnSite', 'SocialShares',
    'EmailOpens', 'EmailClicks', 'PreviousPurchases', 'LoyaltyPoints',
    'Conversion'
]]
corr_matrix = numeric_df.corr()
print(corr_matrix)

plt.figure(figsize=(12, 10))  # Optional: Bigger size for better readability
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-0.3, vmax=0.3)  
plt.title("Correlation Heatmap")
plt.savefig('heatmap_by_CampaignChannel.png')
plt.show()


