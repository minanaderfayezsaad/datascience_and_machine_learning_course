import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pandas.read_csv("D:/dr wael data science/digital_marketing_campaign_dataset.csv")

coulmn_to_analyze=["Age","Income","AdSpend","ClickThroughRate","ConversionRate","WebsiteVisits","PagesPerVisit","TimeOnSite","SocialShares","EmailOpens","EmailClicks","PreviousPurchases","LoyaltyPoints"]
x=df['Age']
print("\n 1 statistic for Age:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())


x=df['Income']
print("\n 2 statistic for Income:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['AdSpend']
print("\n 3 statistic for AdSpend:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['ClickThroughRate']
print("\n 4 statistic for ClickThroughRate:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['ConversionRate']
print("\n 5 statistic for ConversionRate:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['WebsiteVisits']
print("\n 6 statistic for WebsiteVisits:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['PagesPerVisit']
print("\n 7 statistic for PagesPerVisit:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['TimeOnSite']
print("\n 8 statistic for TimeOnSite:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())


x=df['SocialShares']
print("\n 9 statistic for SocialShares:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['EmailOpens']
print("\n 10 statistic for EmailOpens:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['EmailClicks']
print("\n 11 statistic for EmailClicks:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())

x=df['PreviousPurchases']
print("\n 12 statistic for PreviousPurchases:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min(),)
print("\n maximum:",x.max(),)

x=df['LoyaltyPoints']
print("\n 13 statistic for LoyaltyPoints:")
print("\n sum:",x.sum())
print("\n avarage:",x.mean())
print("\n minimum:",x.min())
print("\n maximum:",x.max())