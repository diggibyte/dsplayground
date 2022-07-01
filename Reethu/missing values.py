import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
print(df.shape)

#dropna
print(df.dropna())
print(df.dropna(how = 'all'))#drop rows whose all data is missin
print(df.dropna(how = 'any')) #drop rows with atleast one null value
print(df.dropna(how = 'all',axis = 1))#drop columns whose all data is missing
print(df.dropna(how = 'any',axis = 1))#drop column with atleast one data is missing
print(df.dropna(thresh = 32)) #here it will drop dose rows which dont have 32 nonnull values

#replace
print(df.replace(to_replace='NaN', value = 'XYZ'))