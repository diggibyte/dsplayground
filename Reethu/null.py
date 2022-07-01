import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
print(df.isnull())
print(df[df['country'].isnull()].iloc[:4,13:16])
print(df.isnull().sum())#to find no.of null values in each column
print(df.isnull().sum().sum())#to find no.of null values in the data set

#to fill null values
print(df.fillna('XYZ'))
df1 = df['country'].isin({'XYZ'})
print(df1)
print(df[df1])