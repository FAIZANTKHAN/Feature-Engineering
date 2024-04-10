import  pandas as pd
#Outlier Detection And Removal Using Percentile
#Height data(simple data)
df=pd.read_csv("heights.csv")
            #Detect outlier using percetile
max_thresold=df['height'].quantile(0.95)
#print(max_thresold)
print(df[df['height']>max_thresold])  #The data which is greater than the max  thresold
min_thresold=df['height'].quantile(0.05)
#print(min_thresold)
print(df[df['height']<min_thresold])  #The data which is less than the min  thresold

#Remove the outlier
#print(df[(df['height']<max_thresold) &(df['height']>min_thresold)])  #The data which lie between min and max thresold

    #Banglore Property Prices Dataset(Complex data)

df=pd.read_csv("bhp.csv")
#print(df.head())
#print(df.shape)   #(13200,7)

#print(df.describe())

#Explore samples that are above 99.90% percentile and below 1% percentile rank

min_thresold,max_thresold=df.price_per_sqft.quantile([0.001,0.999])

print(min_thresold,max_thresold)

#print(df[df.price_per_sqft<min_thresold])  #Data with price_per_sqft less than min thresold
#print(df[df.price_per_sqft>max_thresold]) #Data with price _per_sqft more than max thresold

df2=df[(df.price_per_sqft<max_thresold) &(df.price_per_sqft>min_thresold)]  #Data Points between max_thresold and min_thresold
print(df2.head(10))




