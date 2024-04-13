import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("bhp.csv")
#print(df.head())

#Using percentiles as a upper and lower bound
min_thresold,max_thresold=df.price_per_sqft.quantile([0.001,0.999])
#print(min_thresold, max_thresold) #1366.18  ,50956.362
df1=df[(df.price_per_sqft>min_thresold)&(df.price_per_sqft<max_thresold)]
#print(df1.head())  #Data points where price is in between min and max thresold


#Using Std deviation as outlier removal
upper_limit=df1.price_per_sqft.mean()+4*df1.price_per_sqft.std()
lower_limit=df1.price_per_sqft.mean()-4*df1.price_per_sqft.std()
#print(lower_limit,upper_limit)

#print(df1[(df1.price_per_sqft>upper_limit)|(df1.price_per_sqft<lower_limit)].sample(10))
#Outof  range data points

df3=df1[(df1.price_per_sqft<upper_limit)&(df1.price_per_sqft>lower_limit)]  #In between the range
#print(df3.shape)
#print(df.shape)
plt.hist(df3.price_per_sqft,bins=20,rwidth=0.8)
plt.xlabel('Price per square ft')
plt.ylabel('Count')
#plt.show()

#Lets draw the bell curve
from scipy.stats import norm
import numpy as np

plt.hist(df3.price_per_sqft,bins=20,rwidth=0.8,density=True)
plt.xlabel('Height(inches)')
plt.ylabel("Count")

rng=np.arange(-5000,df3.price_per_sqft.max(),100)
plt.plot(rng,norm.pdf(rng,df3.price_per_sqft.mean(),df3.price_per_sqft.std()))
#plt.show()

#Now using Z score for outlier removal
df1['zscore']=(df1.price_per_sqft-df1.price_per_sqft.mean())/df1.price_per_sqft.std()
outliers_z=df1[(df1.zscore<-4)|(df1.zscore>4)]
#print(outliers_z.shape)  #125,8

#Dataframe without any ouliers
df4=df1[(df1.zscore>-4)&(df1.zscore<4)]
print(df4.shape)#13074,8  we remove 125 outliers
