import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
print(df)
# first 5 rows
print(df.head(5))
# to know the column
print(df.columns)
#to know the length
print(len(df))
#to know the data types
print(df.dtypes)
# to select columns with particular data types
print(df.select_dtypes(include = 'int64'))
print(df.select_dtypes(exclude = 'int64'))
#to insert new column
random_col = np.random.randint(100,size = len(df))
df.insert(3,'Random_col',int,allow_duplicates= False)
print(df.iloc[1:3,2:6])
print(df.columns)



