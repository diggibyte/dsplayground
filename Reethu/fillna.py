import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
print(df.isnull())
print(df[df['country'].isnull()].iloc[:4,13:16])
print(df.isnull().sum())#to find no.of null values in each column
print(df.isnull().sum().sum())#to find no.of null values in the data set

#to fill null values
print(df.fillna('XYZ'))
df1 = [df['country'].isin({'XYZ'})]
print(df1)

#pad
print(df.fillna(method = 'pad'))
print(df.fillna(method = 'pad',axis =1))#copy value from column before it
print(df.isnull().sum())#if we add inplace true in ablove line it will show dat there is nonull value in df bcz its making changes to d original dataframe

#bfill
print(df.fillna(method = 'bfill'))
print(df.fillna(method = 'bfill',axis = 1))

#filling with mean,max or min
print(df.fillna(value= df['babies'].mean()))
print(df.fillna(value=df['babies'].max()))
print(df.fillna(df['babies'].min(),inplace = True))
print(df.isnull().sum().sum())





