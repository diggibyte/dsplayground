import pandas as pd
import numpy as np
df = pd.read_csv("E:\DB\Data set.csv")
print(df.where(df['hotel']== 'Resort Hotel',0).head(10))
print(df['hotel'].where(df['adults'] <2,0).head(5))
filter1 = df['hotel'] == 'City Hotel'
filter2 = df['country'] =='RUS'
print(df.where(filter1 & filter2))