import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
df['rank'] = df['country'].rank()
print(df['rank'].head())
print(df.sort_values('hotel').head())

#isin method
print(df['country'].unique())
df1 = df['country'].isin(['RUS','PRT','GBR'])
print(df1)
print(df[df1])
print(df[df1].iloc[:,12:16])

#replace method
print(df.babies.unique())
print(df.babies.replace(10,3))
print(df.babies.replace(10,3).unique())
print(df.babies.replace({10:3,9:2}).unique())

#rename
print(df.rename(columns= {'hotel':'hotel_name'}).head(5))
print(df.rename(columns= {'hotel':'hotel_name','is_canceled':'canceled'}).iloc[0:4,0:3])
