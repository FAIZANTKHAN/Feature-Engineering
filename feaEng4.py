import pandas as pd
import numpy as np

df=pd.read_csv("heights.csv")
#So IQR is interquantile range like Q1 means 25th percentile...and so on
#print(df.describe())
Q1=df.height.quantile(0.25)
Q3=df.height.quantile(0.75)
IQR=Q3-Q1 #IQR is Q3-Q1
#print(IQR)  #5.66

#We have to find lower and upper limit

lower_range=Q1-1.5*IQR
upper_range=Q3+1.5*IQR

#print(lower_range, upper_range)  #55.00 and 77.67
print(df[(df.height<lower_range)|(df.height>upper_range)]) #Data points out of ranges

print(df[(df.height>lower_range)&(df.height<upper_range)].head(10)) #Data points between the range only 10 points