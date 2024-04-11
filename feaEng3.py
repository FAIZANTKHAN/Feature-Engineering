#Outlier Detection and Removal Using Z-score and standard deviation in python pandas
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df=pd.read_csv("heights.csv")
#print(df.sample(5))

plt.hist(df.height,bins=20,rwidth=0.8)
plt.xlabel('Height(inches)')
plt.ylabel('Count')
#plt.show()  #It is normal distribution


#Plot bell curve along with histogram for our dataset

from scipy.stats import norm
import numpy as np
plt.hist(df.height,bins=20,rwidth=0.8,density=True)
plt.xlabel('Height(inches)')
plt.ylabel('Count')

rng=np.arange(df.height.min(),df.height.max(),0.1)
plt.plot(rng,norm.pdf(rng,df.height.mean(),df.height.std()))
#plt.show()

#print(df.height.mean())  #66.36


#print(df.height.std())  #3.84
#Outlier detection and removal using 3 standard deviation
#Use 3 std deviation as lower and upper bound to remove the outliers

upper_limit=df.height.mean()+3*df.height.std()
#print(upper_limit)#77.91

lower_limit=df.height.mean()-3*df.height.std()
#print(lower_limit)#54.82

#Data points beyond 3 std deviation from mean
print(df[(df.height>upper_limit)|(df.height<lower_limit)])

#Now remove these outliers and generate new dataframe
df_no_outlier_std_dev=df[(df.height<upper_limit)&(df.height>lower_limit)]
#print(df_no_outlier_std_dev.head())
#print(df_no_outlier_std_dev.shape)
#print(df.shape)  #We delete the 7 ouliers from the original dataframe

# Outlier detection and removal using Z Score

df['zscore']=(df.height-df.height.mean())/df.height.std()  #adding a new colun withnthe z score of every point

#print(df.head(5))
#print(df[df['zscore']>3])  #printing the data points which are above 3 std dev
#print(df[df['zscore']<-3])  #printing the data points which are less than -3 std dev

#print(df[(df.zscore<-3) | (df.zscore>3)])  #Printing both above and below the 3 std dev

#Lets remove the outliers and save it into a new data frame
df_no_outlier=df[(df.zscore >-3)&(df.zscore<3)]
print(df_no_outlier.head())

print(df_no_outlier.shape)
print(df.shape)
#same as part 1 we have remove the 7 outliers