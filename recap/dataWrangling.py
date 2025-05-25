import pandas as pd

df1 = pd.read_csv("programming/datascience/data/mexico-real-estate-1.csv")
df2 = pd.read_csv("programming/datascience/data/mexico-real-estate-2.csv")
df3 = pd.read_csv("programming/datascience/data/mexico-real-estate-3.csv")

###To clean the data we will remove columns with NaN values, remove $ and commas from price
## and convert price to float

df1.dropna() # removes rows with NaN values
df1.dropna(how='all') #removes rows whose all values are NaN
df1.dropna(axis=1) #remces columns with at least one NaN value
df1.dropna(axis=1, how='all') #removes columns whose all values are NaN
df1.dropna(subset=['price']) #removes rows with NaN values in the 'price' column

### to remove $ and commas from price
df1['price'] = df1['price'].str.replace('$','').str.replace(',', '').astype(float)



### Removing NaN in df2 as well as converting price in pessos to price in dollars

#removing NaN values in df2
df2 = df2.dropna(inplace=True)

#converting price in pessos to price in dollars, we will create a new column for price in dollars

df2["price_dollars"] = (df2["price_mxn"]/19).round(2) #assuming 1 dollar = 19 pesos, we round to 2 decimal places

#the we drop the price_mxn column
df2 = df2.drop(column =["price_mxn"], inplace=True)